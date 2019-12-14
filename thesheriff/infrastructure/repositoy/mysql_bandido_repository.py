"""
.. module:: bandido_mysql_repository
   :platform: Windows,Unix
   :synopsis: Bandido MySQL Repository

.. moduleauthor:: The Sheriff Team <thesheriff@team.net>


"""
from thesheriff.domain.bandido.repository.bandido_repository import BandidoRepository
from thesheriff.domain.bandido import Bandido
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, ForeignKey, Float
)

from typing import NoReturn

metadata = MetaData()

bandido = Table('bandidos', metadata,
                Column('id', Integer, primary_key=True, autoincrement=True),
                Column('puntuacion', Float, nullable=False),
                Column('bandas', ForeignKey('bandas.id'), nullable=False),
                Column('bandas_puntuacion', ForeignKey('bandas.id')))


class BandidoMySQLRepository(BandidoRepository):
    """BandidoMySQLRepository implements persistence for Bandido on MySQL.

    :param database_uri: URI for connecting to MySQL
    :type database_uri: str.
    :return: NoReturn.
    """

    def __init__(self, database_uri: str) -> NoReturn:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def of_id(self, bandido_id: int) -> Bandido:
        """of_id searches for a Bandido matching bandido_id
        :param bandido_id: ID of the Bandido to be returned.
        :type bandido_id: int.
        :return: Bandido.
        """
        query = bandido.select().where(bandido.c.id == bandido_id)
        return self.__connection.execute(query)

    def add(self, new_bandido: Bandido) -> NoReturn:
        """Add persists a new Bandido to MySQL.
        :param new_bandido: Object with the Bandido information
        :type new_bandido: Bandido.
        :return: NoReturn.
        """
        query = bandido.insert().value(**new_bandido)
        self.__connection.execute(query)

    def update(self, mod_bandido: Bandido) -> NoReturn:
        """Update modifies existing Bandidos
        :param mod_bandido: Object with Bandido information to be updated.
        :type mod_bandido: Bandido.
        :return: NoReturn.
        """
        query = bandido.update().where(
            bandido.c.id == mod_bandido.id).values(**mod_bandido)
        self.__connection.execute(query)

    def remove(self, bandido_id: int) -> NoReturn:
        """Remove deletes existing Bandido

        :param bandido_id: ID of the Bandido to be removed.
        :type bandido_id: int.
        :return: NoReturn.
        """
        query = bandido.delete().where(bandido.c.id == bandido_id)
        self.__connection.execute(query)

    def lista_amigos(self, bandido_id: int) ->list<Bandido>:
        """Lists bandido's friends

                :param bandido_id: ID of the Bandido to list his friends
                :type bandido_id: int.
                :return: list<Bandido>.
                """
        query = bandido.select().where(bandido.c.id == bandido_id)
        return self.__connection.execute(query)



