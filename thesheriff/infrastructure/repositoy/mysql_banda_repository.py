"""
.. module:: banda_mysql_repository
   :platform: Windows,Unix
   :synopsis: Banda MySQL Repository

.. moduleauthor:: The Sheriff Team <thesheriff@team.net>


"""
from typing import NoReturn

from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer,
    ForeignKey
)

from thesheriff.domain.banda.banda import Banda
from thesheriff.domain.banda.repository.banda_repository import BandaRepository

metadata = MetaData()

banda_table = Table('banda', metadata,
                    Column('id', Integer, primary_key=True, autoincrement=True),
                    Column('puntuacion', Integer, nullable=False),
                    Column('miembros', ForeignKey('bandidos.id')))


class BandaMySQLRepository(BandaRepository):

    def __init__(self, database_uri: str) -> NoReturn:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def of_id(self, banda_id: int) -> Banda:
        query = banda_table.select().where(banda_table.c.id == banda_id)

        return self.__connection.execute(query)

    def all(self) -> [Banda]:
        query = banda_table.select()

        return self.__connection.execute(query)

    def add(self, nueva_banda: Banda) -> NoReturn:
        query = banda_table.insert().value(**nueva_banda)
        self.__connection.execute(query)

    def update(self, mod_banda: Banda) -> NoReturn:
        query = banda_table.update().where(
            banda_table.c.id == mod_banda.id).values(**mod_banda)
        self.__connection.execute(query)

    def remove(self, banda_id: int) -> NoReturn:
        query = banda_table.delete().where(banda_table.c.id == banda_id)
        self.__connection.execute(query)
