from thesheriff.domain.asalto.asalto_repository import AsaltoRepository
from thesheriff.domain.asalto import Asalto

from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, Text, DateTime, \
        insert
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

asalto = Table('asaltos', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('sheriff_id', Text, nullable=False),
              Column('lugar', Text, nullable=False),
              Column('miembros', relationship("Bandido"), nullable=False),
              Column('fecha', DateTime, nullable=False))

class AsaltoMySQLRepository(AsaltoRepository):
    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def add(self, nuevo_asalto: Asalto) -> None:
        query = asalto.insert().value(**nuevo_asalto)
        self.__connection.execute(query)

    def update(self, mod_asalto: Asalto) -> None:
        query = asalto.update().where(
            asalto.c.id == mod_asalto.id).values(**mod_asalto)
        self.__connection.execute(query)

    def remove(self, asalto_id: int) -> None:
        query = asalto.delete().where(asalto.c.id == asalto_id)
        self.__connection.execute(query)