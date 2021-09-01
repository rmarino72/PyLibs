import time

from RMLibs.basic.BasicObject import BasicObject
from RMLibs.util.DateTimeUtil import DateTimeUtil
from farsight.bo.Coordinates import Coordinates
from farsight.bo.Packet import Packet
from farsight.bo.WallHumidity import WallHumidity
from farsight.client.FSWSClient import FSWSClient
from farsight.config.Config import Config
from farsight.dao.Sample import Sample
from farsight.database.FSDbManager import FSDbManager
from farsight.utils.Utils import Utils


class DataProducer(BasicObject):

    __db: FSDbManager
    __config: Config

    @property
    def db(self) -> FSDbManager:
        return self.__db

    @db.setter
    def db(self, db: FSDbManager):
        self.__db = db

    @property
    def config(self) -> Config:
        return self.__config

    @config.setter
    def config(self, config: Config):
        self.__config = config


    def __produce(self):
        try:
            sample: Sample = Sample()

            coordinates: Coordinates = Utils.get_coordinates()
            sample.latitude = coordinates.latitude
            sample.latitude = coordinates.longitude

            sample.ambient_humidity = Utils.get_ambient_humidity()
            sample.cpu_temperature = Utils.get_cpu_temperature()

            wall_humidity: WallHumidity = Utils.get_wall_humidity()
            sample.ch0_wall_humidity = wall_humidity.ch0_wall_humidity
            sample.ch1_wall_humidity = wall_humidity.ch1_wall_humidity
            sample.ch2_wall_humidity = wall_humidity.ch2_wall_humidity

            sample.timestamp = DateTimeUtil.get_now()

            self.debug_verbose(".run(self) - storing sample: \n " + sample.to_json())

            self.__db.store_obj(sample)
            self.__db.delete_old_samples(DateTimeUtil.add_days(DateTimeUtil.get_now(),
                                                               -self.__config.obsolete_days))
        except Exception as ex:
            self.error(".__produce(self) - " + str(ex))
            raise ex

    def __consume(self):
        try:
            res = self.__db.get_unsent_samples()
            for sample in res:

                packet = Packet()
                packet.type = "SAMPLE"
                packet.id = sample.id
                packet.latitude = sample.latitude
                packet.longitude = sample.longitude
                packet.timestamp = sample.timestamp
                packet.cpu_temperature = sample.cpu_temperature
                packet.ambient_humidity = sample.ambient_humidity
                packet.ch0_wall_humidity = sample.ch0_wall_humidity
                packet.ch1_wall_humidity = sample.ch1_wall_humidity
                packet.ch2_wall_humidity = sample.ch2_wall_humidity
                packet.sent = sample.sent

                packet.uid = self.config.uid
                packet.mac_address = self.config.mac_address

                client: FSWSClient = FSWSClient()

                client.logger = self.logger
                client.db = self.db
                client.config = self.config
                client.url = "ws://"+self.config.server_ip+":"+str(self.config.server_port)
                client.timeout = 5

                try:
                    client.connect()
                    client.send(packet.to_json())
                    client.close_connection()

                except Exception as ex:
                    self.error(".__consume - " + str(ex) )

        except Exception as ex:
            self.error(".__consume(self) - " + str(ex))
            raise ex

    def run(self):
        self.info(".run(self) - Running producer")
        timeout = self.__config.producer_timeout

        while True:
            try:
                self.__produce()
                self.__consume()
                time.sleep(timeout)

            except Exception as ex:
                self.error(".run(self) - " + str(ex))
