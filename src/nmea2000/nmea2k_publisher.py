#-------------------------------------------------------------------------------
# Name:        nmea2000_publishers
# Purpose:     Publishers to debug and trace NMEA2000
#
# Author:      Laurent Carré
#
# Created:     25/10/2021
# Copyright:   (c) Laurent Carré Sterwen Technology 2021-2022
# Licence:     Eclipse Public License 2.0
#-------------------------------------------------------------------------------

import logging
import datetime
import time
import os
from nmea_routing.publisher import Publisher
from nmea2000.nmea2k_pgndefs import *
from nmea_routing.filters import FilterSet
from nmea2000.nmea2k_decode_dispatch import get_n2k_decoded_object, N2KMissingDecodeEncodeException
from nmea_data.nmea_statistics import N2KStatistics, NMEA183Statistics

from nmea_routing.generic_msg import *
from nmea_routing.configuration import NavigationConfiguration
from utilities.global_variables import find_pgn


_logger = logging.getLogger("ShipDataServer" + "." + __name__)


class PgnRecord:

    def __init__(self, pgn: int):
        self._pgn = pgn
        self._pgn_def = find_pgn(pgn)
        self._clock = time.time()
        self._count = 1

    @property
    def pgn(self):
        return self._pgn

    @property
    def pgn_def(self):
        return self._pgn_def

    def tick(self):
        self._count += 1


class N2KTracePublisher(Publisher):

    def __init__(self, opts):
        super().__init__(opts)
        filter_names = opts.getlist('filters', str)
        self._flexible = opts.get('flexible_decode', bool, True)
        if filter_names is not None and len(filter_names) > 0:
            _logger.info("Publisher:%s filter set:%s" % (self.name(), filter_names))
            self._filters = FilterSet(filter_names)
            self._filter_select = True
        self._print_option = opts.get('output', str, 'ALL')
        _logger.info("%s output option %s" % (self.name(), self._print_option))
        self._trace_fd = None
        filename = opts.get('file', str, None)
        if filename is not None and self.is_active:
            trace_dir = NavigationConfiguration.get_conf().get_option('trace_dir', '/var/log')
            date_stamp = datetime.datetime.now().strftime("%y%m%d-%H%M")
            filename = "%s-N2K-%s.log" % (filename, date_stamp)
            filepath = os.path.join(trace_dir, filename)
            _logger.info("Opening trace file %s" % filepath)
            try:
                self._trace_fd = open(filepath, "w")
            except IOError as e:
                _logger.error("Trace file error %s" % e)
                self._trace_fd = None
        self._stats = N2KStatistics()

    def process_msg(self, gen_msg):
        if gen_msg.type != N2K_MSG:
            return True
        msg = gen_msg.msg
        _logger.debug("Trace publisher input msg %s" % msg.format2())
        if self._print_option == 'NONE':
            return True
        '''
        if self._filters is not None:
            if not self._filters.process_filter(msg, execute_action=False):
                return True
        '''
        # print("decoding %s", msg.format1())
        if self._flexible:
            try:
                res = msg.decode()
            except N2KDecodeException:
                return True
            except Exception as e:
                _logger.error("Error decoding PGN: %s message:%s" % (e, msg.format1()))
                return True
        else:
            try:
                res = get_n2k_decoded_object(msg)
            except N2KMissingDecodeEncodeException:
                self._stats.add_entry(msg)
                return True
            except Exception as e:
                _logger.error("Error decoding PGN: %s message:%s" % (e, msg.format1()))
                return True

        _logger.debug("Trace publisher msg:%s" % res)
        if res is not None:
            if self._print_option in ('ALL', 'PRINT'):
                print("Message:", res.as_json())
            if self._print_option in ('ALL', 'FILE') and self._trace_fd is not None:
                # self._trace_fd.write("Message from SA:%d " % msg.sa)
                self._trace_fd.write(res.as_json())
                self._trace_fd.write('\n')
        return True

    def stop(self):
        print("List of missing decode for PGN")
        self._stats.print_entries()
        if self._trace_fd is not None:
            self._trace_fd.close()
        super().stop()


class N2KStatisticPublisher(Publisher):

    def __init__(self, opts):
        super().__init__(opts)
        self._n183_stats = NMEA183Statistics()
        self._n2k_stats = N2KStatistics()

    def process_msg(self, msg: NavGenericMsg):
        if msg.type == N0183_MSG:
            self._n183_stats.add_entry(msg.talker(), msg.formatter())
        else:
            self._n2k_stats.add_entry(msg.msg)
        return True

    def stop(self):
        self._n183_stats.print_entries()
        self._n2k_stats.print_entries()
        super().stop()


