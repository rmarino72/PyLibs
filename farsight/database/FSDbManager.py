import json
from datetime import datetime

from RMLibs.database.SQLiteManager import SQLiteManager
from RMLibs.logging.RMLogger import RMLogger
from RMLibs.util.DateTimeUtil import DateTimeUtil

from farsight.config.Config import Config
from farsight.dao.Sample import Sample


class FSDbManager (SQLiteManager):

    def __init__(self, config: Config, logger: RMLogger):
        super().__init__()
        self.logger = logger
        self.__initialize(config)

    def __initialize(self,  config: Config):
        self.debug_verbose("Initializing database...")
        self.file_name = config.db_file
        self.open_connection()
        self.create_table_if_not_exists(Sample().get_table(self.metadata))

    def update_sample(self, sample: Sample):
        try:
            self.debug_verbose(".update_sample(self, sample: Sample) - Updating sample: \n " + sample.to_json())
            update_obj = sample.get_update(self.metadata)
            self._conn.execute(update_obj.where(update_obj.table.c.id == sample.id))
        except Exception as ex:
            self.error(".update_sample(self, id: int) - " + str(ex))
            raise ex

    def delete_old_samples(self, timestamp: datetime):
        try:
            self.debug_verbose(".delete_old_samples(self, timestamp: str) - Deleting objects with timestamp <= " +
                               DateTimeUtil.datetime_to_string(timestamp))
            del_obj = Sample().get_delete(self.metadata)
            self._conn.execute(del_obj.where(del_obj.table.c.timestamp <= timestamp))
        except Exception as ex:
            self.error(".delete_old_samples(self, timestamp: str) - " + str(ex))
            raise ex

    def get_unsent_samples(self) -> list:
        result = []
        try:
            table = Sample().get_table(self.metadata)
            select = table.select().where(table.c.sent == 0)
            res: list = self._conn.execute(select)

            for row in res:
                sample = Sample()
                sample.from_rs(row)
                result.append(sample)

            return result
        except Exception as ex:
            self.error(".get_unsent_samples(self) - " + str(ex))
            raise ex

    def get_sample_by_id(self, id: int) -> Sample or None:

        result: [Sample] = []
        try:
            table = Sample().get_table(self.metadata)
            select = table.select().where(table.c.id == id)
            res: list = self._conn.execute(select)

            for row in res:
                sample = Sample()
                sample.from_rs(row)
                result.append(sample)

            if len(result) == 0:
                return None
            return result[0]
        except Exception as ex:
            self.error(".get_sample_by_id(self, id: int) - " + str(ex))
            raise ex