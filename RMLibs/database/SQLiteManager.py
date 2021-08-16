# install SQLAlchemy

import sqlalchemy.engine

from RMLibs.basic.BasicObject import BasicObject
import sqlalchemy as db

from RMLibs.database.BasicDao import BasicDao


class SQLiteManager(BasicObject):
    """
    SQLite database manager
    """

    __PREFIX = "sqlite:///"

    __file_name: str or None = None
    __connected: bool = False
    _conn: sqlalchemy.engine.Connection or None = None
    __engine: sqlalchemy.engine.Engine or None = None

    @property
    def file_name(self) -> str:
        """
        :return: the name of the SQLite database file
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name: str):
        """
        sets the name of the SQLite database file
        :param file_name: full path to the db file
        """
        self.__file_name = file_name

    @property
    def connected(self) -> bool:
        """
        :return: True if the connection to the db is open
        """
        return self.__connected

    @property
    def metadata(self) -> sqlalchemy.MetaData:
        if not self.connected:
            raise Exception("The connection is not open")
        return db.MetaData(self.__engine)

    def __del__(self):
        """
        Destructor
        """
        if self.connected:
            self.close_connection()

    def open_connection(self):
        """
        Opens the connection to the database file
        """
        try:
            if self.connected:
                raise Exception("The connection is open yet")
            self.__engine = db.create_engine(self.__PREFIX + self.file_name)
            self._conn = self.__engine.connect()
            self.__connected = True
        except Exception as ex:
            self.error('.open_connection(self) - ' + str(ex))
            raise ex

    def close_connection(self):
        """
        Closes the open connection
        """
        try:
            if not self.connected:
                raise Exception("The connection is not open")
            self._conn.close()
            self.__connected = False
        except Exception as ex:
            self.error('.close_connection(self) - ' + str(ex))
            raise ex

    def create_table_if_not_exists(self, table: sqlalchemy.Table):
        try:
            if not self.connected:
                raise Exception("The connection is not open")
            if not self.__engine.dialect.has_table(self._conn, table.name):
                self.debug_verbose(".create_table_if_not_exists(self, table: sqlalchemy.Table) - Creating table " + table.name)
                table.metadata.create_all()
            else:
                self.debug_verbose(".create_table_if_not_exists(self, table: sqlalchemy.Table) - Table " + table.name + " already exists")
        except Exception as ex:
            self.error('.create_table_if_not_exists(self, table: sqlalchemy.Table) - ' + str(ex))
            raise ex

    def store_obj(self, obj: BasicDao):
        try:
            self._conn.execute(obj.get_insert(self.metadata))
        except Exception as ex:
            self.error(".store_obj(self, obj: BasicDao) - " + str(ex))
            raise ex

    def update_obj(self, obj: BasicDao):
        try:
            self._conn.execute(obj.get_update(self.metadata))
        except Exception as ex:
            self.error(".update_obj(self, obj: BasicDao) - " + str(ex))
            raise ex