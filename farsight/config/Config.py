from RMLibs.basic.BasicObject import BasicObject


class Config(BasicObject):

    __db_file: str or None
    __log_path: str or None
    __debug_level: str or None
    __verbose: str or None
    __mac_address: str
    __uid: str
    __consumer_timeout: int
    __producer_timeout: int
    __obsolete_days: int
    __server_ip: str or None
    __server_port: int

    @property
    def db_file(self) -> str:
        return self.__db_file

    @db_file.setter
    def db_file(self, db_file: str):
        self.__db_file = db_file

    @property
    def log_path(self) -> str:
        return self.__log_path

    @log_path.setter
    def log_path(self, log_path: str):
        self.__log_path = log_path

    @property
    def debug_level(self) -> str:
        return self.__debug_level

    @debug_level.setter
    def debug_level(self, debug_level: str):
        self.__debug_level = debug_level

    @property
    def verbose(self) -> str:
        return self.__verbose

    @verbose.setter
    def verbose(self, debug_verbose: str):
        self.__verbose = debug_verbose

    @property
    def mac_address(self) -> str:
        return self.__mac_address

    @mac_address.setter
    def mac_address(self, mac_address: str):
        self.__mac_address = mac_address

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def consumer_timeout(self) -> int:
        return self.__consumer_timeout

    @consumer_timeout.setter
    def consumer_timeout(self, consumer_timeout: int):
        self.__consumer_timeout = consumer_timeout

    @property
    def producer_timeout(self) -> int:
        return self.__producer_timeout

    @producer_timeout.setter
    def producer_timeout(self, producer_timeout: int):
        self.__producer_timeout = producer_timeout

    @property
    def obsolete_days(self) -> int:
        return self.__obsolete_days

    @obsolete_days.setter
    def obsolete_days(self, obsolete_days: int):
        self.__obsolete_days = obsolete_days

    @property
    def server_ip(self) -> str:
        return self.__server_ip

    @server_ip.setter
    def server_ip(self, server_ip: str):
        self.__server_ip = server_ip

    @property
    def server_port(self) -> int:
        return self.__server_port

    @server_port.setter
    def server_port(self, server_port: int):
        self.__server_port = server_port

    def __init__(self, file_name: str):
        super().__init__()
        with open(file_name) as config_file:
            text = config_file.read()
            self.from_json(text)
