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
import os
from nmea_routing.publisher import Publisher
from nmea2000.nmea2k_pgndefs import *
from nmea_routing.filters import FilterSet


from nmea_routing.generic_msg import *
from nmea_routing.configuration import NavigationConfiguration


_logger = logging.getLogger("ShipDataServer" + "." + __name__)


class PgnRecord:

    def __init__(self, pgn: int, clock: int):
        self._pgn = pgn
        self._pgn_def = PGNDefinitions.pgn_defs().pgn_def(pgn)
        self._clock = clock
        self._count = 1

    @property
    def pgn(self):
        return self._pgn

    @property
    def pgn_def(self):
        return self._pgn_def

    def tick(self):
        self._count += 1

    def check(self, clock, interval) -> bool:
        if clock - self._clock >= interval:
            self._clock = clock
            return True
        else:
            return False

    def __str__(self):
        if self._pgn == 0:
            return "Dummy PGN 0"
        else:
            return "PGN %d|%04X|%s|count:%d" % (self._pgn, self._pgn, self._pgn_def, self._count)


class N2KProbePublisher(Publisher):

    def __init__(self, opts):
        _logger.info("Instantiating N2KProbePublisher")
        self._interval = int(opts['interval']) * 1e9
        self._records = {}
        super().__init__(opts)

    def process_msg(self, gen_msg):
        # print("Process msg pgn", msg.pgn)
        if gen_msg.type != N2K_MSG:
            return
        msg = gen_msg.msg
        clock = time.time_ns()
        display = False
        if msg.pgn == 0:
            return False
        try:
            rec = self._records[msg.pgn]
        except KeyError:
            display = True
            rec = PgnRecord(msg.pgn, clock)
            self._records[msg.pgn] = rec
        else:
            rec.tick()
            if rec.check(clock, self._interval):
                display = True
        if display:
            print(rec)
        return True

    def dump_records(self):
        for rec in self._records.values():
            print(rec)


class N2KTracePublisher(Publisher):

    def __init__(self, opts):
        super().__init__(opts)
        filter_names = opts.getlist('filters', str)
        if filter_names is not None and len(filter_names) > 0:
            _logger.info("Publisher:%s filter set:%s" % (self.name(), filter_names))
            self._filters = FilterSet(filter_names)
        self._print_option = opts.get('output', str, 'ALL')
        _logger.info("%s output option %s" % (self.name(), self._print_option))
        self._trace_fd = None
        filename = opts.get('file', str, None)
        if filename is not None:
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

    def process_msg(self, gen_msg):
        if gen_msg.type != N2K_MSG:
            return True
        msg = gen_msg.msg
        if self._print_option == 'NONE':
            return True
        if self._filters is not None:
            if not self._filters.process_filter(msg, execute_action=False):
                return True
        # print("decoding %s", msg)
        try:
            res = msg.decode()
        except N2KDecodeException:
            return True
        # _logger.debug("Trace publisher msg:%s" % res)
        if res is not None:
            if self._print_option in ('ALL', 'PRINT'):
                print(res)
            if self._print_option in ('ALL', 'FILE') and self._trace_fd is not None:
                self._trace_fd.write(str(res))
                self._trace_fd.write('\n')
        return True

    def stop(self):
        if self._trace_fd is not None:
            self._trace_fd.close()
        super().stop()


def pgn_list(str_filter):
    res = []
    str_pgn_list = str_filter.split(',')
    pgn_defs = PGNDefinitions.pgn_defs()
    for str_pgn in str_pgn_list:
        pgn = int(str_pgn)
        try:
            pgn_d = pgn_defs.pgn_def(pgn)
        except N2KUnknownPGN:
            print("Invalid PGN:", pgn, "Ignored")
            continue
        res.append(pgn)
    return res
