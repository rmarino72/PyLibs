from datetime import datetime
from sqlalchemy import Table, Column, Integer, Float, DateTime, MetaData

from RMLibs.database.BasicDao import BasicDao


class Sample(BasicDao):

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

    def __init__(self):
        self.__id = -1
        self.__latitude = 0.0
        self.__longitude = 0.0
        self.__timestamp = None
        self.__cpu_temperature = 0.0
        self.__ambient_humidity = 0.0
        self.__ch0_wall_humidity = 0.0
        self.__ch1_wall_humidity = 0.0
        self.__ch2_wall_humidity = 0.0
        self.__sent = 0

    def get_table(self, metadata: MetaData) -> Table:
        return Table("Sample", metadata,
                     Column('id', Integer, primary_key=True),
                     Column('latitude', Float),
                     Column('longitude', Float),
                     Column('timestamp', DateTime),
                     Column('cpu_temperature', Float),
                     Column('ambient_humidity', Float),
                     Column('ch0_wall_humidity', Float),
                     Column('ch1_wall_humidity', Float),
                     Column('ch2_wall_humidity', Float),
                     Column('sent', Integer),
                     sqlite_autoincrement=True)

    def get_insert(self, metadata: MetaData):
        table: Table = self.get_table(metadata)
        values: dict = self.to_dict()
        del values['id']
        return table.insert().values(values)
