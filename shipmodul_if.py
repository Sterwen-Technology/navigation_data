#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Laurent
#
# Created:     14/04/2019
# Copyright:   (c) Laurent 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket
import sys

from argparse import ArgumentParser
import threading
import queue
import logging
import time
import datetime

import nmea0183

def _parser():
    p = ArgumentParser(description=sys.argv[0])

    p.add_argument("-p", "--port", action="store", type=int,
                   default=10110,
                   help="Listening port for Shipmodul input, default is 10110")
    p.add_argument("-a", "--address", action="store", type=str,
                   default='',
                   help="IP address or URL for Shipmodul, no default")
    p.add_argument("-pr", "--protocol", action="store", type=str,
                   choices=['TCP','UDP'], default='TCP',
                   help="Protocol to read NMEA sentences, default TCP")
    p.add_argument("-s", "--server", action="store", type=int,
                   default=4500,
                   help="NMEA server port, default 4500")
    p.add_argument('-d', '--trace_level', action="store", type=str,
                   choices=["CRITICAL","ERROR", "WARNING", "INFO", "DEBUG"],
                   default="INFO",
                   help="Level of traces, default INFO")
    p.add_argument('-cp', '--config_port', action="store", type=int,
                   default=4501,
                   help="port for Shipmodul configuration server, default 4501")
    p.add_argument("-t", "--timeout", action="store", type=float,
                   default=30.0,
                   help="Timeout on reception of messages from Shipmodul, default 30sec")
    p.add_argument("-m", "--max_connections", action="store", type=int, default=16,
                   help="Maximum number of simultaneous connections on server, default 16"
                   )
    p.add_argument("-b", "--heartbeat", action="store", type=float,
                   default=60.0,
                   help="Active connection heartbeat period, default 60.0s")
    return p


parser = _parser()
_logger = logging.getLogger("ShipDataServer")


class Options(object):
    def __init__(self, p):
        self.parser = p
        self.options = None

    def __getattr__(self, name):
        if self.options is None:
            self.options = self.parser.parse_args()
        try:
            return getattr(self.options, name)
        except AttributeError:
            raise AttributeError(name)


class ShipModulInterface(threading.Thread):
    def __init__(self, address, port, timeout=30.0):
        super().__init__()
        self._address = address
        self._port = port
        self._publishers = []
        self._configmode = False
        self._configpub = None
        self._startTS = 0
        self._total_msg = 0
        self._last_msg_count = 0
        self._timeout = timeout

    def close(self):
        self._socket.close()

    def timer_lapse(self):
        _logger.debug("Timer lapse => total number of messages:%g" % self._total_msg)
        if self._total_msg-self._last_msg_count == 0:
            # no message received
            _logger.warning("No NMEA messages received in the last %4.1f sec" % self._timeout)
        self._last_msg_count = self._total_msg
        t = threading.Timer(self._timeout, self.timer_lapse)
        t.start()

    def run(self):
        self._startTS = time.time()
        t = threading.Timer(self._timeout, self.timer_lapse)
        t.start()
        while True:
            try:
                data = self.read()
                _logger.debug(data.decode().strip('\n\r'))
                if len(data) == 0:
                    _logger.warning("No data from shipmodul => stop connection")
                    break
            except KeyboardInterrupt:
                break
            self._total_msg += 1
            self.publish(data)
        self.close()

    def register(self, pub):
        self._publishers.append(pub)

    def deregister(self, pub):
        if pub == self._configpub:
            self._configmode = False
            self._configpub = None
            _logger.info("Switching to normal mode for Shipmodul")
        else:
            try:
                self._publishers.remove(pub)
            except ValueError:
                _logger.warning("Removing non attached publisher %s" % pub.descr())
                pass

    def publish(self, msg):
        if self._configmode:
            self._configpub.publish(msg)
        else:
            for p in self._publishers:
                p.publish(msg)

    def configModeOn(self, pub):
        if len(self._address) < 4:
            _logger.error("Missing target IP address for config mode")
            return False
        else:
            self._configmode = True
            self._configpub = pub
            _logger.info("Switching to configuration mode for Shipmodul")
            return True


class UDP_reader(ShipModulInterface):
    def __init__(self,address, port):
        super().__init__(address, port)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        try:
            self._socket.bind(('',port))
        except OSError as e:
            _logger.error("Error connecting Shipmodul via UDP:%s" % str(e))
            raise

    def read(self):
        data, address = self._socket.recvfrom(256)
        # print(data)
        return data

    def send(self, msg):
        try:
            self._socket.sendto(msg,(self._address, self._port))
        except OSError as e:
            _logger.critical("Error writing on Shipmodul: %s" % str(e))
            raise


class TCP_reader(ShipModulInterface):

    def __init__(self,address,port):
        super().__init__(address, port)
        try:
            self._socket = socket.create_connection((address, port))
        except OSError as e:
            _logger.error("Connection error with shipmodul using TCP: %s" % str(e))
            raise

    def read(self):
        try:
            msg = self._socket.recv(256)
        except OSError as e:
            _logger.critical("Error receiving from Shipmodul: %s" % str(e))
            raise
        # print(msg)
        return msg

    def send(self, msg):
        try:
            self._socket.sendall(msg)
        except OSError as e:
            _logger.critical("Error writing to  Shipmodul: %s" % str(e))
            raise


class Publisher(threading.Thread):
    '''
    Super class for all publishers
    '''
    def __init__(self):
        super().__init__()


class NMEA_Publisher(Publisher):

    def __init__(self, client, reader):
        super().__init__()
        self._client = client
        self._reader = reader
        self._queue = queue.Queue(20)
        client.add_publisher(self)
        # reader.register(self)

    def run(self):
        while True:
            msg = self._queue.get()
            if self._client.send(msg):
                self._client.close()
                break

    def publish(self, msg):
        try:
            self._queue.put(msg, block=False)
        except queue.Full:
            # need to empty the queue
            _logger.warning("Overflow on connection %s" % self._client.descr())
            try:
                discard = self._queue.get(block=False)
            except queue.Empty:
                pass
            self.publish(msg)

    def deregister(self):
        self._reader.deregister(self)

    def descr(self):
        return self._client.descr()


class ClientConnection:
    def __init__(self, connection, address, server):
        self._socket = connection
        self._address = address
        self._server = server
        self._totalmsg = 0
        self._periodmsg = 0
        self._pubs = []

    def send(self,msg):
        try:
            self._socket.sendall(msg)
            self._totalmsg += 1
            self._periodmsg += 1
            return False
        except OSError as e:
            _logger.warning(
                "Error writing data on %s:%d connection:%s => STOP" % (self._address[0], self._address[1], str(e)))
            return True

    def close(self):
        for p in self._pubs:
            p.deregister()
        self._socket.close()
        self._server.remove_client(self._address)

    def reset_period(self):
        self._periodmsg = 0

    def msgcount(self):
        return self._periodmsg

    def add_publisher(self, pub):
        self._pubs.append(pub)

    def descr(self):
        return "Connection %s:%d" % self._address


class NMEA_server(threading.Thread):
    def __init__(self, port, reader, options):
        super().__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('0.0.0.0', port))
        self._reader = reader
        self._options = options
        self._connections = {}

    def run(self):
        _logger.info("Data server ready")
        t = threading.Timer(self._options.heartbeat, self.heartbeat)
        t.start()
        while True:
            _logger.info("Data server waiting for new connection")
            self._socket.listen(1)
            if len(self._connections) <= self._options.max_connections:
                connection, address = self._socket.accept()
            else:
                _logger.critical("Maximum number of connections (%d) reached => Server stop" % self._options.max_connections)
                break

            _logger.info("New connection from IP %s port %d" % address)
            client = ClientConnection(connection, address, self)
            pub = NMEA_Publisher(client, self._reader)
            self._reader.register(pub)
            self._connections[address] = client
            pub.start()

    def remove_client(self, address):
        del self._connections[address]

    def heartbeat(self):
        _logger.info("Server heartbeat number of connections: %d" % len(self._connections))
        t = threading.Timer(self._options.heartbeat, self.heartbeat)
        t.start()
        to_be_closed = []
        for client in self._connections.values():
            if client.msgcount() == 0:
                # no message during period
                _logger.info("Sending heartbeat on %s" % client.descr())
                heartbeat_msg = nmea0183.ZDA().message()
                if client.send(heartbeat_msg):
                    to_be_closed.append(client)
                client.reset_period()
        for client in to_be_closed:
            client.close()


class ShipModulConfig(threading.Thread):

    def __init__(self, port, reader):
        super().__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('0.0.0.0', port))
        self._reader = reader
        self._pub = None

    def run(self):
        _logger.info("Configuration server ready")
        while True:
            _logger.info("Configuration server waiting for new connection")
            self._socket.listen(1)
            connection, address = self._socket.accept()
            _logger.info("New configuration connection from %s:%d" % address)
            pub = NMEA_Publisher(connection, self._reader, self, address)
            if not self._reader.configModeOn(pub):
                connection.close()
                continue
            self._pub = pub
            pub.start()
            _logger.info("Shipmodul configuration active")
            while pub.is_alive():
                try:
                    msg = connection.recv(256)
                    if len(msg) == 0:
                        break
                except OSError as e:
                    _logger.info("config socket read error: %s" % str(e))
                    break
                try:
                    self._reader.send(msg)
                except OSError:
                    break
            _logger.info("Connection with configuration application lost")
            self._reader.deregister(pub)
            connection.close()


def main():
    opts = Options(parser)
    # looger setup => stream handler for now
    loghandler = logging.StreamHandler()
    logformat = logging.Formatter("%(asctime)s | [%(levelname)s] %(message)s")
    loghandler.setFormatter(logformat)
    _logger.addHandler(loghandler)
    _logger.setLevel(opts.trace_level)

    nmea0183.NMEA0183Sentences.init('SN')
    # open the shipmodul port
    port = opts.port
    address = opts.address
    try:
        if opts.protocol == "UDP":
            _logger.info("opening UDP port %d" % port)
            reader = UDP_reader(address, port)
        else:

            _logger.info("opening port on host %s port %d" % (address, port))
            reader = TCP_reader (address, port)
            _logger.info("listening for NMEA sentences on host %s port %d" % (address, port))
    except OSError:
        return
    except Exception as e:
        _logger.critical(str(e))
        return

    server = NMEA_server(opts.server, reader, opts)
    config_server = ShipModulConfig(opts.config_port, reader)
    server.start()
    config_server.start()
    reader.start()
    try:
        reader.join()
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
