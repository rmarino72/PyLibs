import sqlalchemy.sql.roles
from sqlalchemy import Table, MetaData
from RMLibs.basic.BasicObject import BasicObject


class BasicDao(BasicObject):

    def get_table(self, metadata: MetaData) -> Table:
        name: str = self.class_name
        return Table(name, metadata)

    def get_insert(self, metadata: MetaData):
        return self.get_table(metadata).insert()

    def get_update(self, metadata: MetaData):
        values: dict = self.to_dict()
        return self.get_table(metadata).update().values(values)

    def get_delete (self, metadata: MetaData):
        return self.get_table(metadata).delete()

    def from_rs(self, rs):
        values: dict = self.to_dict()
        for key in values.keys():
            exec ("self." + key + " = rs." + key)
