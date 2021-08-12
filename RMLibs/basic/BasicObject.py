import json
from RMLibs.logging.RMLogger import RMLogger


class BasicObject:

    __logger: RMLogger = None

    @property
    def logger(self) -> RMLogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: RMLogger):
        self.__logger = logger

    @staticmethod
    def json_to_dict(json_str: str) -> dict:
        """
        Converts a json string to a dict
        :param json_str: the json string
        :return: the dict
        """
        return json.loads(json_str)

    @staticmethod
    def object_list_to_dict_list(object_list: list) -> list:
        res: list = []
        for obj in object_list:  # type: BasicObject
            res.append(obj.to_dict())
        return res

    @staticmethod
    def object_list_to_json(object_list: list) -> str:
        dict_list: list = BasicObject.object_list_to_dict_list(object_list)
        return json.dumps(dict_list)

    def __compose_debug_msg(self, msg: str) -> str:
        return type(self).__name__ + msg

    def debug(self, msg: str):
        self.__logger.debug(self.__compose_debug_msg(msg))

    def debug_verbose(self, msg: str):
        self.logger.debug(self.__compose_debug_msg(msg), True)

    def info(self, msg: str):
        self.__logger.info(self.__compose_debug_msg(msg))

    def error(self, msg: str):
        self.__logger.error(self.__compose_debug_msg(msg))

    def to_json(self) -> str or None:
        """
        converts the Basic Object to a JSON String
        :return: the json String
        """
        try:
            obj: dict = self.__dict__.copy()
            if "_BasicObject__logger" in obj.keys():
                del obj["_BasicObject__logger"]
            res: str = json.dumps(obj, sort_keys=True, indent=4).replace(
                '_' + type(self).__name__ + '__', '')
            return res
        except Exception as ex:
            self.error('.to_json(self) - an error has occurred: ' + str(ex))
            return None

    def to_dict(self) -> dict or None:
        """
        Converts the Business Object to a Dict
        :return: the dict
        """
        try:
            return self.json_to_dict(self.to_json())
        except Exception as ex:
            self.error('.to_dict(self) - an error has occurred: ' + str(ex))
            return None

    def from_json(self, json_str: str):
        """
        Loads the Basic Object property values from a json string
        :param json_str: the json string
        """
        try:
            obj_dict: dict = json.loads(json_str)
            for key in obj_dict.keys():
                exec('self.' + key + ' = obj_dict["' + key + '"]')
        except Exception as ex:
            self.error('.from_json(self, json_str: str) - an error has occurred: ' + str(ex))