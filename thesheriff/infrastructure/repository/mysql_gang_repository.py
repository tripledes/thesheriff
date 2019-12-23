"""
thesheriff.infrastructure.repository.mysql_gang_respository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements Gang MySQL Repository.
"""
from typing import NoReturn, List
from sqlalchemy import create_engine, MetaData, Table
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository


class MySQLGangRepository(GangRepository):
    """MySQLGangRepository implements persistence for Gang on MySQL.

    :param database_uri: URI for connecting to MySQL.
    :type database_uri: String
    """

    def __init__(self, database_uri: str, meta: MetaData, gang_table: Table):
        engine = create_engine(database_uri)
        self.__connection = engine.connect()
        self.__gang_table = gang_table
        meta.create_all(self.__connection)

    def of_id(self, gang_id: int) -> Gang:
        """of_id searches for a Gang matching gang_id.

        :param gang_id: ID of the Gang to be returned.
        :type gang_id: Integer
        :return: Gang object.
        :rtype: Gang
        """
        query = self.__gang_table.select().where(
            self.__gang_table.c.id == gang_id)

        return self.__connection.execute(query)

    def all(self) -> List[Gang]:
        """all returns all Gangs stored on MySQL.

        :return: List Gang objects.
        :rtype: List[Gang]
        """
        # TODO(all): iterate on the returned rows and call
        # GangFactory, return GangCollection (TBI)
        query = self.__gang_table.select()

        return self.__connection.execute(query)

    def add(self, new_gang: Gang) -> NoReturn:
        """Method add persists a new Gang to MySQL.

        :param new_gang: Object with the new Gang details.
        :type new_gang: Gang
        :return: No returned value.
        :rtype: NoReturn
        """
        query = self.__gang_table.insert()\
            .values(owner_id=new_gang.owner_id, name=new_gang.name)
        self.__connection.execute(query)

    def update(self, mod_gang: Gang) -> NoReturn:
        """Method update modifies existing Gang.

        :param mod_gang: Object with Gang details to be updated.
        :type mod_gang: Gang
        :return: No returned value.
        :rtype: NoReturn
        """
        query = self.__gang_table.update().where(
            self.__gang_table.c.id == mod_gang.id).values(**mod_gang)
        self.__connection.execute(query)

    def remove(self, gang_id: int) -> NoReturn:
        """Method remove deletes existing Gang.

        :param gang_id: Id of the Gang to be removed.
        :type gang_id: Integer
        :return: No returned value.
        :rtype: NoReturn
        """
        query = self.__gang_table.delete().where(
            self.__gang_table.c.id == gang_id)
        self.__connection.execute(query)
