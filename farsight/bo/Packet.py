from RMLibs.basic.BasicObject import BasicObject
from datetime import datetime

class Packet(BasicObject):

    __type: str
    __mac_address: str
    __uid: str
    __id: int
    __latitude: float
    __longitude: float
    __timestamp: datetime or None
    __cpu_temperature: float
    __ambient_humidity: float
    __ch0_wall_humidity: float
    __ch1_wall_humidity: float
    __ch2_wall_humidity: float
    __sent: int

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude

    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self.__longitude = longitude

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        self.__timestamp = timestamp

    @property
    def cpu_temperature(self) -> float:
        return self.__cpu_temperature

    @cpu_temperature.setter
    def cpu_temperature(self, cpu_temperature: float):
        self.__cpu_temperature = cpu_temperature

    @property
    def ambient_humidity(self) -> float:
        return self.__ambient_humidity

    @ambient_humidity.setter
    def ambient_humidity(self, ambient_humidity: float):
        self.__ambient_humidity = ambient_humidity

    @property
    def ch0_wall_humidity(self) -> float:
        return self.__ch0_wall_humidity

    @ch0_wall_humidity.setter
    def ch0_wall_humidity(self, ch0_wall_humidity: float):
        self.__ch0_wall_humidity = ch0_wall_humidity

    @property
    def ch1_wall_humidity(self) -> float:
        return self.__ch1_wall_humidity

    @ch1_wall_humidity.setter
    def ch1_wall_humidity(self, ch1_wall_humidity: float):
        self.__ch1_wall_humidity = ch1_wall_humidity

    @property
    def ch2_wall_humidity(self) -> float:
        return self.__ch2_wall_humidity

    @ch2_wall_humidity.setter
    def ch2_wall_humidity(self, ch2_wall_humidity: float):
        self.__ch2_wall_humidity = ch2_wall_humidity

    @property
    def sent(self) -> int:
        return self.__sent

    @sent.setter
    def sent(self, sent: int):
        self.__sent = sent

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
