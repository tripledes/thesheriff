"""
.. module:: asalto_mysql_repository
   :platform: Windows,Unix
   :synopsis: Asalto MySQL Repository

.. moduleauthor:: The Sheriff Team <thesheriff@team.net>


"""
from thesheriff.domain.asalto.asalto_repository import AsaltoRepository
from thesheriff.domain.asalto import Asalto
from typing import NoReturn
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, Text, DateTime,
    ForeignKey, insert
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

asalto = Table('asaltos', metadata,
               Column('id', Integer, primary_key=True, autoincrement=True),
               Column('sheriff_id', Text, nullable=False),
               Column('lugar', Text, nullable=False),
               # Column('miembros', Integer, ForeignKey('bandidos.id')),
               # FIXME(tripledes) here goes a relationship but no idea how to do it
               # without sqlalchemy core (no ORM)
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

    def add(self, nuevo_asalto: Asalto) -> NoReturn:
        """Add persists a new Asalto to MySQL.

        :param nuevo_asalto: Object with the Asalto information
        :type nuevo_asalto: Asalto.
        :return: NoReturn.
        """
        query = asalto.insert().value(**nuevo_asalto)
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

    def remove(self, asalto_id: int) -> NoReturn:
        """Remove deletes existing Asaltos

        :param asalto_id: ID of the Asalto to be removed.
        :type asalto_id: int.
        :return: NoReturn.
        """
        query = asalto.delete().where(asalto.c.id == asalto_id)
        self.__connection.execute(query)
