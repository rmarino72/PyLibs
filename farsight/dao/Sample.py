from RMLibs.basic.BasicObject import BasicObject


class Sample(BasicObject):
    __latitude: float

    def __init__(self):
        self.__latitude = 0.0


    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude