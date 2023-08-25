#-------------------------------------------------------------------------------
# Name:        Log utilities
# Purpose:     Set of functions to manage logs
#
# Author:      Laurent Carré
#
# Created:     01/08/2023
# Copyright:   (c) Laurent Carré Sterwen Technology 2021-2023
# Licence:     Eclipse Public License 2.0
#-------------------------------------------------------------------------------

import logging
import os

_logger = logging.getLogger("ShipDataServer")


class NavigationLogSystem:

    loghandler = None

    @staticmethod
    def adjust_log_level(config):
        '''
        Adjust the log level for each individual module (file)
        :param config:
        :return:
        '''
        modules = config.get_option('log_module', None)
        if modules is None:
            return
        # print(modules)
        for module, level in modules.items():
            mod_log = _logger.getChild(module)
            if mod_log is not None:
                mod_log.setLevel(level)
            else:
                _logger.error("Module %s non-existent" % module)

    @staticmethod
    def create_log():
        NavigationLogSystem.loghandler = logging.StreamHandler()
        logformat = logging.Formatter("%(asctime)s | [%(levelname)s] %(message)s")
        NavigationLogSystem.loghandler.setFormatter(logformat)
        _logger.addHandler(NavigationLogSystem.loghandler)
        _logger.setLevel('INFO')

    @staticmethod
    def finalize_log(config):
        log_file = config.get_option("log_file", None)
        if log_file is not None:
            log_dir = config.get_option('trace_dir', None)
            if log_dir is not None:
                log_fullname = os.path.join(log_dir, log_file)
            else:
                log_fullname = log_file
            try:
                fp = open(log_fullname, 'w')
                NavigationLogSystem.loghandler.setStream(fp)
            except IOError as e:
                _logger.error("Error opening log file %s %s" % (log_fullname, e))
                pass

        _logger.setLevel(config.get_option('log_level', 'INFO'))
        NavigationLogSystem.adjust_log_level(config)

