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

    def delete_old_samples(self, timestamp: datetime):
        try:
            self.debug_verbose("delete_old_samples(self, timestamp: str) - Deleting objects with timestamp <= " +
                               DateTimeUtil.datetime_to_string(timestamp))
            self._conn.execute(Sample().get_delete_old_samples(timestamp, self.metadata))
        except Exception as ex:
            self.error(".delete_old_samples(self, timestamp: str) - " + str(ex))
            raise ex