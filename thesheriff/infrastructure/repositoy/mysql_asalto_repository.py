"""
.. module:: asalto_mysql_repository
   :platform: Windows,Unix
   :synopsis: Asalto MySQL Repository
.. moduleauthor:: The Sheriff Team <thesheriff@team.net>
"""
from thesheriff.domain.asalto.repository.asalto_repository import AsaltoRepository
from thesheriff.domain.asalto import Asalto
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, Text, DateTime,
    ForeignKey
)

from typing import NoReturn

metadata = MetaData()

asalto = Table('asaltos', metadata,
               Column('id', Integer, primary_key=True, autoincrement=True),
               Column('sheriff_id', Text, nullable=False),
               Column('lugar', Text, nullable=False),
               Column('miembros', ForeignKey('bandidos.id')),
               Column('fecha', DateTime, nullable=False))


class AsaltoMySQLRepository(AsaltoRepository):
    """AsaltoMySQLRepository implements persistence for Asalto on MySQL.
    :param database_uri: URI for connecting to MySQL
    :type database_uri: str.
    :return: NoReturn.
    """

    def __init__(self, database_uri: str) -> NoReturn:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def of_id(self, asalto_id: int) -> Asalto:
        """of_id searches for an Asalto matching asalto_id
        :param asalto_id: ID of the Asalto to be returned.
        :type asalto_id: int.
        :return: Asalto.
        """
        query = asalto.select().where(asalto.c.id == asalto_id)
        return self.__connection.execute(query)

    def add(self, new_asalto: Asalto) -> NoReturn:
        """Add persists a new Asalto to MySQL.
        :param new_asalto: Object with the Asalto information
        :type new_asalto: Asalto.
        :return: NoReturn.
        """
        query = asalto.insert().value(**new_asalto)
        self.__connection.execute(query)

    def update(self, mod_asalto: Asalto) -> NoReturn:
        """Update modifies existing Asaltos
        :param mod_asalto: Object with Asalto information to be updated.
        :type mod_asalto: Asalto.
        :return: NoReturn.
        """
        query = asalto.update().where(
            asalto.c.id == mod_asalto.id).values(**mod_asalto)
        self.__connection.execute(query)
