import logging
import datetime
import traceback
from logging import Logger

from RMLibs.util.StringUtils import StringUtils


class RMLogger:
    """
    Implementation of a customized logger
    """
    __file_name: str or None
    __log_path: str or None
    __last_date: str or None
    __logger: Logger
    __verbose: bool

    __levels: list = [logging.DEBUG, logging.INFO, logging.ERROR]

    # . Logging level DEBUG
    DEBUG = logging.DEBUG

    # . Logging level INFO
    INFO = logging.INFO

    # . Logging level ERROR
    ERROR = logging.ERROR

    def __init__(self):
        """
        Constructor
        """
        self.__file_name = None
        self.__log_path = None
        self.__last_date = None
        self.__logger = logging.getLogger('RMLogger')
        self.__verbose = False

    def __repr__(self):
        return self

    def __compose_file_name(self) -> str or None:
        if StringUtils.empty_string(self.file_name):
            return None
        fn: str = str(datetime.date.today()).replace('-', '') + '-' + self.file_name + '.log'
        if not StringUtils.empty_string(self.__log_path):
            fn = self.log_path + '/' + fn
        return fn.replace('//', '/')

    def __verify_file_name(self):
        if self.__file_name is not None:
            today: str = str(datetime.date.today())
            if today != self.__last_date:
                self.__last_date = today
                for h in self.__logger.handlers:
                    self.__logger.removeHandler(h)
                handler = logging.FileHandler(self.__compose_file_name())
                self.__logger.addHandler(handler)

    @staticmethod
    def __get_log_time_header() -> str:
        return '[' + datetime.datetime.now().time().strftime('%I:%M:%S') + '] - '

    @staticmethod
    def __compose_message(msg: str, level=logging.DEBUG):

        lvl = ''
        if level == RMLogger.DEBUG:
            lvl = 'DEBUG'
        if level == RMLogger.ERROR:
            lvl = 'ERROR'
        if level == RMLogger.INFO:
            lvl = 'INFO'

        message: str = RMLogger.__get_log_time_header() + lvl + ' - ' + msg
        print(message)
        if level == RMLogger.ERROR:
            traceback.print_exc()
        return message

    @property
    def level(self) -> int:
        """
        :return the logging level
        """
        return self.__logger.level

    @level.setter
    def level(self, level: int):
        """
        Sets the logging leve
        :param level: the logging level
        """
        if level not in self.__levels:
            raise Exception('Invalid log level')
        self.__logger.setLevel(level)

    @property
    def file_name(self) -> str:
        """
        :return the file name
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name: str):
        """
        Sets the file name
        :param file_name: the file name
        """
        self.__file_name = file_name

    @property
    def log_path(self) -> str:
        """
        :return the log path
        """
        return self.__log_path

    @log_path.setter
    def log_path(self, log_path: str):
        """
        Sets the log path
        :param log_path: the log path
        :return:
        """
        self.__log_path = log_path

    @property
    def verbose(self) -> bool:
        """
        :return True if verbose mode is on
        """
        return self.__verbose

    @verbose.setter
    def verbose(self, verbose: bool):
        """
        Sets the verbose mode
        :param verbose: True or False whether the verbose mode is on or off
        """
        self.__verbose = verbose

    def info(self, msg: str):
        """
        Logs at INFO level
        :param msg: the message to log
        """
        self.__verify_file_name()
        self.__logger.info(RMLogger.__compose_message(msg, RMLogger.INFO))

    def debug(self, msg: str, verbose: bool = False):
        """
        Logs at DEBUG level
        :param msg: the message to log
        :param verbose: True if the message must be logged only if the Verbose mode is on
        """
        self.__verify_file_name()
        if not verbose or (verbose and self.verbose):
            self.__logger.debug(RMLogger.__compose_message(msg, RMLogger.DEBUG))

    def error(self, msg: str):
        """
        Logs at ERROR level
        :param msg: the message to log
        """
        self.__verify_file_name()
        self.__logger.error(RMLogger.__compose_message(msg, RMLogger.ERROR))
