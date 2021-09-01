from RMLibs.basic.BasicObject import BasicObject


class WallHumidity(BasicObject):

    __ch0_wall_humidity: float
    __ch1_wall_humidity: float
    __ch2_wall_humidity: float

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

    def __init__(self):

        self.__ch0_wall_humidity = 0.0
        self.__ch1_wall_humidity = 0.0
        self.__ch2_wall_humidity = 0.0
