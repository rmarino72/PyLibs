from RMLibs.basic.BasicObject import BasicObject


class Config(BasicObject):

    __db_file: str or None
    __log_path: str or None
    __debug_level: str or None
    __verbose: str or None

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

    def __init__(self, file_name: str):
        super().__init__()
        with open(file_name) as config_file:
            text = config_file.read()
            self.from_json(text)
