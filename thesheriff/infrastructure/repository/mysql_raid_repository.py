"""
thesheriff.infrastructure.repository.mysql_raid_respository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements Raid MySQL Repository.
"""
from typing import List, NoReturn
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.raid.raid_factory import RaidFactory
from thesheriff.domain.raid.repository.raid_repository import \
    RaidRepository
from thesheriff.domain.outlaw.outlaw_factory import OutlawFactory
from thesheriff.domain.gang.gang_factory import GangFactory
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from sqlalchemy import create_engine, MetaData, Table


class MySQLRaidRepository(RaidRepository):
    """MySQLRaidRepository implements persistence for Raid on MySQL.

    :param database_uri: URI for connecting to MySQL
    :type database_uri: String
    """

    def __init__(self, database_uri: str, meta: MetaData, raid_table: Table):
        engine = create_engine(database_uri)
        self.__connection = engine.connect()
        self.__raid_table = raid_table
        meta.create_all(self.__connection)

    def of_id(self, raid_id: int) -> Outlaw:
        """Method of_id searches for an Raid matching raid_id.

        :param raid_id: Id of the Raid to be returned.
        :type raid_id: Integer
        :return: The Raid matching raid_id.
        :rtype: Raid
        """
        # FIXME(tripledes)
        # Use GangFactory and OutlawFactory for both gang and members.
        query = self.__raid_table.select().where(
            self.__raid_table.c.id == raid_id)
        result = self.__connection.execute(query)
        members = self.__split_outlaws_ids(result.get('members'))
        outlaws = self.__create_outlaws_from_ids(members)
        # gang = GangFactory.create()
        return RaidFactory.create(
            id=result.get('id'),
            name=result.get('name'),
            outlaws=outlaws,
            sheriff=result.get('sheriff_id'),
            gang=result.get('gang_id'),
            location=result.get('location'),
            date=result.get('date'))

    def add(self, new_raid: Raid) -> NoReturn:
        """Method add persists a new Outlaw to MySQL.

        :param new_outlaw: Object with the Outlaw information.
        :type new_outlaw: Outlaw
        :return: No returned value.
        :rtype: NoReturn
        """

        outlaws_ids = self.__find_outlaws_ids()
        query = self.__raid_table.insert().values(
            sheriff_id=new_raid.sheriff.id,
            gang_id=new_raid.gang.id,
            name=new_raid.name,
            members=outlaws_ids,
        )
        self.__connection.execute(query)

    def update(self, mod_raid: Raid) -> NoReturn:
        """Method update updates an existing Raid.
        :param mod_raid: Object with the Raid information
        :type mod_raid: Raid.
        :return: NoReturn.
        """
        query = self.__raid_table.update().where(
            self.__raid_table.c.id == mod_raid.id).values(**mod_raid)
        self.__connection.execute(query)

    def __join_bandidos_ids(self):
        ids = [bandido.id for bandido in self.bandidos]
        return ','.join(ids)

    def __split_outlaws_ids(self, outlaws: str) -> List[int]:
        ids = outlaws.split(',')
        return [int(id) for id in ids]

    def __create_outlaws_from_ids(self, members: list) -> List[Outlaw]:
        # results = list()
        #  for member in members:
        #     results.append(
        #         OutlawFactory.create(
        #         )
        #     )
        pass