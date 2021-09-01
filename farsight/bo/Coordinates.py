from RMLibs.basic.BasicObject import BasicObject


class Coordinates(BasicObject):

    __latitude: float
    __longitude: float

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

    def __init__(self):
        self.__latitude = 0.0
        self.__longitude = 0.0

