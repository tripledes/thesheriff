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
import sys


class MySQLRaidRepository(RaidRepository):
    """MySQLRaidRepository implements persistence for Raid on MySQL.

    :param database_uri: URI for connecting to MySQL
    :type database_uri: String
    """

    def __init__(self, database_uri: str, meta: MetaData, raid_table: Table):
        engine = create_engine(database_uri, pool_pre_ping=True)
        self.__connection = engine.connect()
        self.__raid_table = raid_table
        meta.create_all(self.__connection)

    def of_id(self, raid_id: int) -> Raid:
        """Method of_id searches for an Raid matching raid_id.

        :param raid_id: Id of the Raid to be returned.
        :type raid_id: Integer
        :return: The Raid matching raid_id.
        :rtype: Raid
        """
        # FIXME(all) need to create Gang and List[Outlaw]
        # for returning a complete Raid
        query = self.__raid_table.select().where(
            self.__raid_table.c.id == raid_id)
        result = self.__connection.execute(query)
        row = result.fetchone()
        members = self.__split_outlaws_ids(row.members)
        outlaws = self.__create_outlaws_from_ids(members)
        # gang = GangFactory.create()
        # create outlaws
        # create Sheriff
        return RaidFactory.create(
            id=result.get('id'),
            name=result.get('name'),
            outlaws=outlaws,
            sheriff=result.get('sheriff_id'),
            gang=result.get('gang_id'),
            location=result.get('location'),
            date=result.get('date')
        )

    def add(self, new_raid: Raid) -> Raid:
        """Method add persists a new Raid to MySQL.

        :param new_raid: Object with the Raid information.
        :type new_raid: Raid
        :return: The inserted Raid with informed id attribute.
        :rtype: Raid
        """

        outlaw_ids = self.__join_outlaw_ids(new_raid.outlaws)
        query = self.__raid_table.insert().values(
            sheriff_id=new_raid.sheriff.id,
            gang_id=new_raid.gang.id,
            name=new_raid.name,
            location=new_raid.location,
            members=outlaw_ids,
            date=new_raid.date
        )
        result = self.__connection.execute(query)
        new_raid.id = result.lastrowid
        return new_raid

    def update(self, mod_raid: Raid) -> NoReturn:
        """Method update updates an existing Raid.

        :param mod_raid: Object with the Raid information
        :type mod_raid: Raid.
        :return: No returned value.
        :rtype: NoReturn
        """
        query = self.__raid_table.update().where(
            self.__raid_table.c.id == mod_raid.id).values(**mod_raid)
        self.__connection.execute(query)

    def __join_outlaw_ids(self, outlaws: List[Outlaw]) -> str:
        ids = [str(outlaw.id) for outlaw in outlaws]
        return ','.join(ids)

    def __split_outlaw_ids(self, outlaws: str) -> List[int]:
        ids = outlaws.split(',')
        return [int(id) for id in ids]

    def __create_outlaw_from_ids(self, members: list) -> List[Outlaw]:
        # results = list()
        #  for member in members:
        #     results.append(
        #         OutlawFactory.create(
        #         )
        #     )
        pass
