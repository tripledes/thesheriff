from thesheriff.domain.outlaw.repository.outlaw_repository import OutlawRepository
from thesheriff.domain.outlaw.outlaw import Outlaw
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, ForeignKey, Float
)
from typing import NoReturn, List

METADATA = MetaData()

outlaw_table = Table('outlaws', METADATA,
                     Column('id', Integer, primary_key=True, autoincrement=True),
                     Column('score', Float, nullable=False),
                     Column('gangs', ForeignKey('gangs.id'), nullable=False),
                     Column('gangs_score', ForeignKey('gangs.id')))


class MySQLOutlawRepository(OutlawRepository):
    """MySQLOutlawRepository implements persistence for Outlaw on MySQL.

    :param database_uri: URI for connecting to MySQL
    :type database_uri: str.
    """

    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def of_id(self, outlaw_id: int) -> Outlaw:
        """Method of_id searches for a Outlaw matching outlaw_id
        :param outlaw_id: ID of the Outlaw to be returned.
        :type outlaw_id: Integer.
        :returns: Outlaw -- The outlaw matching outlaw_id.
        """
        query = outlaw_table.select().where(outlaw_table.c.id == outlaw_id)
        return self.__connection.execute(query)

    def add(self, new_outlaw: Outlaw) -> NoReturn:
        """Method add persists a new Outlaw to MySQL.
        :param new_outlaw: Object with the new Outlaw details
        :type new_outlaw: Outlaw.
        :returns: NoReturn -- No returned value.
        """
        query = outlaw_table.insert().value(**new_outlaw)
        self.__connection.execute(query)

    def update(self, mod_outlaw: Outlaw) -> NoReturn:
        """Method update modifies existing Outlaw
        :param mod_outlaw: Object with Outlaw details to be updated.
        :type mod_outlaw: Outlaw.
        :return: NoReturn -- No returned value.
        """
        query = outlaw_table.update().where(
            outlaw_table.c.id == mod_outlaw.id).values(**mod_outlaw)
        self.__connection.execute(query)

    def remove(self, outlaw_id: int) -> NoReturn:
        """Method remove deletes existing Outlaw
        :param outlaw_id: Id of the Outlaw to be removed.
        :type outlaw_id: Integer.
        :returns: NoReturn -- No returned value.
        """
        query = outlaw_table.delete().where(outlaw_table.c.id == outlaw_id)
        self.__connection.execute(query)

    def get_friends(self, outlaw_id: int) -> List[Outlaw]:
        """Method get_Friends lists outlaw's friends
        :param outlaw_id: Id of the Outlaw to list his friends
        :type outlaw_id: Integer.
        :returns: List[Outlaw] -- The list of friends.
        """
        query = outlaw_table.select().where(outlaw_table.c.id == outlaw_id)
        return self.__connection.execute(query)



