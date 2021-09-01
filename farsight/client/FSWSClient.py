import json
from RMLibs.websocket.WSClient import WSClient
from farsight.config.Config import Config
from farsight.dao.Sample import Sample
from farsight.database.FSDbManager import FSDbManager

class FSWSClient(WSClient):

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

    def received(self, content: str):
        self.debug_verbose(".received(self, content: str) - RECEIVED: " + content)
        response: dict = json.loads(content)
        if response['type'] == 'REPLY':

            if response['outcome'] == 'OK':
                sample: Sample = self.__db.get_sample_by_id(response['packet_id'])
                if sample is not None:
                    sample.sent = 1
                    self.__db.update_sample(sample)
