from typing import NoReturn, List
from sqlalchemy import create_engine, MetaData, Table
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository


class MySQLGangRepository(GangRepository):

    def __init__(self, database_uri: str, meta: MetaData, gang_table: Table):
        engine = create_engine(database_uri)
        self.__connection = engine.connect()
        self.__gang_table = gang_table
        meta.create_all(self.__connection)

    def of_id(self, gang_id: int) -> Gang:
        query = self.__gang_table.select().where(
            self.__gang_table.c.id == gang_id)

        return self.__connection.execute(query)

    def all(self) -> List[Gang]:
        # TODO(all): iterate on the returned rows and call
        # GangFactory
        query = self.__gang_table.select()

        return self.__connection.execute(query)

    def add(self, new_gang: Gang) -> NoReturn:
        query = self.__gang_table.insert().value(**new_gang)
        self.__connection.execute(query)

    def update(self, mod_gang: Gang) -> NoReturn:
        query = self.__gang_table.update().where(
            self.__gang_table.c.id == mod_gang.id).values(**mod_gang)
        self.__connection.execute(query)

    def remove(self, gang_id: int) -> NoReturn:
        query = self.__gang_table.delete().where(
            self.__gang_table.c.id == gang_id)
        self.__connection.execute(query)
