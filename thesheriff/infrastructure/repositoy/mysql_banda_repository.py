"""
.. module:: banda_mysql_repository
   :platform: Windows,Unix
   :synopsis: Banda MySQL Repository

.. moduleauthor:: The Sheriff Team <thesheriff@team.net>


"""
from thesheriff.domain.banda.repository.banda_repository import BandaRepository
from thesheriff.domain.banda.banda import Banda
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer,
    ForeignKey
)

from typing import NoReturn

metadata = MetaData()

bandaTable = Table('banda', metadata,
               Column('id', Integer, primary_key=True, autoincrement=True),
               Column('puntuacion', Integer, nullable=False),
               Column('miembros', ForeignKey('bandidos.id')))


class BandaMySQLRepository(BandaRepository):

    def __init__(self, database_uri: str) -> NoReturn:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def of_id(self, banda_id: int) -> Banda:
        query = bandaTable.select().where(bandaTable.c.id == banda_id)

        return self.__connection.execute(query)

    def all(self) -> [Banda]:
        query = bandaTable.select()

        return self.__connection.execute(query)

    def add(self, nueva_banda: Banda) -> NoReturn:

        query = bandaTable.insert().value(**nueva_banda)
        self.__connection.execute(query)

    def update(self, mod_banda: Banda) -> NoReturn:

        query = bandaTable.update().where(
            bandaTable.c.id == mod_banda.id).values(**mod_banda)
        self.__connection.execute(query)

    def remove(self, banda_id: int) -> NoReturn:

        query = bandaTable.delete().where(bandaTable.c.id == banda_id)
        self.__connection.execute(query)
