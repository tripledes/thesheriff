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
from thesheriff.domain.outlaw.sheriff_factory import SheriffFactory
from thesheriff.domain.gang.gang_factory import GangFactory
from sqlalchemy import create_engine, MetaData, Table
from datetime import datetime


class MySQLRaidRepository(RaidRepository):
    """MySQLRaidRepository implements persistence for Raid on MySQL.

    :param database_uri: URI for connecting to MySQL
    :type database_uri: String
    :param meta: MetaData object shared across all MySQL repositories.
    :type meta: sqlalchemy.MetaData
    :param outlaw_table: Table object, represents the Raid table in MySQL.
    :type outlaw_table: sqlalchemy.Table
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
        query = self.__raid_table.select().where(
            self.__raid_table.c.id == raid_id)
        result = self.__connection.execute(query)

        row = result.fetchone()
        members = self.__split_outlaw_ids(row.members)
        outlaws = self.__create_outlaw_from_ids(members)
        gang = GangFactory.create_with_id(row.gang_id)
        rates = list()

        if row.rates:
            rates = self.__split_rates(row.rates)
        dt_str = datetime.strftime(row.date, Raid.DEFAULT_DATETIME_FORMAT)
        outlaw = OutlawFactory.create_with_id(row.sheriff_id)
        sheriff = SheriffFactory.create(outlaw)

        return RaidFactory.create(
            raid_id=row.id,
            name=row.name,
            members=outlaws,
            sheriff=sheriff,
            gang=gang,
            location=row.location,
            date=dt_str,
            rates=rates
        )

    def add(self, new_raid: Raid) -> Raid:
        """Method add persists a new Raid to MySQL.

        :param new_raid: Object with the Raid information.
        :type new_raid: Raid
        :return: The inserted Raid with informed id attribute.
        :rtype: Raid
        """

        outlaw_ids = self.__join_outlaw_ids(new_raid.members)
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

    def update_rates(self, raid: Raid) -> NoReturn:
        """Method update_rates, specialized update that handles rates
        transformation before running the actual update.

        :param raid: Raid to be rated.
        :type raid: Raid
        :return: No returned value.
        :rtype: NoReturn
        """
        # TODO(all): Add justification for this method
        # to the documentation
        string_rates = self.__join_rates(raid.rates)
        query = self.__raid_table.update().where(
            self.__raid_table.c.id == raid.id).values({'rates': string_rates})
        self.__connection.execute(query)

    def __join_outlaw_ids(self, outlaws: List[Outlaw]) -> str:
        ids = [str(outlaw.id) for outlaw in outlaws]
        return ','.join(ids)

    def __split_outlaw_ids(self, outlaws: str) -> List[int]:
        ids = outlaws.split(',')
        return [int(outlaw_id) for outlaw_id in ids]

    def __join_rates(self, rates: List[float]) -> str:
        stringified = [str(rate) for rate in rates]
        return ','.join(stringified)

    def __split_rates(self, rates: str) -> List[float]:
        split_rates = rates.split(",")
        return [float(rate) for rate in split_rates]

    def __create_outlaw_from_ids(self, member_ids: list) -> List[Outlaw]:
        results = list()
        for member_id in member_ids:
            results.append(
                OutlawFactory.create_with_id(
                    member_id
                )
            )
        return results
