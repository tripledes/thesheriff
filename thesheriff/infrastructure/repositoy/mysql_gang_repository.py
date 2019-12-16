from typing import NoReturn, List
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer,
    ForeignKey
)
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository

METADATA = MetaData()

gang_table = Table('gang', METADATA,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('score', Integer, nullable=False),
                   Column('members', ForeignKey('outlaws.id')))


class MySQLGangRepository(GangRepository):

    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def of_id(self, gang_id: int) -> Gang:
        query = gang_table.select().where(gang_table.c.id == gang_id)

        return self.__connection.execute(query)

    def all(self) -> List[Gang]:
        # TODO(all): iterate on the returned rows and call
        # GangFactory
        query = gang_table.select()

        return self.__connection.execute(query)

    def add(self, new_gang: Gang) -> NoReturn:
        query = gang_table.insert().value(**new_gang)
        self.__connection.execute(query)

    def update(self, mod_gang: Gang) -> NoReturn:
        query = gang_table.update().where(
            gang_table.c.id == mod_gang.id).values(**mod_gang)
        self.__connection.execute(query)

    def remove(self, gang_id: int) -> NoReturn:
        query = gang_table.delete().where(gang_table.c.id == gang_id)
        self.__connection.execute(query)
