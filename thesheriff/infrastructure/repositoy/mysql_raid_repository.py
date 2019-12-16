from typing import NoReturn
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.raid.raid_factory import RaidFactory
from thesheriff.domain.raid.repository.raid_repository import RaidRepository
from thesheriff.domain.outlaw.outlaw_factory import OutlawFactory
from thesheriff.domain.gang.gang_factory import GangFactory
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, Text, DateTime
)

METADATA = MetaData()

raid_table = Table('raids', METADATA,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('sheriff_id', Integer, nullable=False),
                   Column('gang_id', Integer, nullable=False),
                   Column('name', Text, nullable=False),
                   Column('location', Text, nullable=False),
                   Column('members', Text, nullable=False),
                   Column('date', DateTime, nullable=False))


class MySQLRaidRepository(RaidRepository):
    """MySQLRaidRepository implements persistence for Raid on MySQL.
    :param database_uri: URI for connecting to MySQL
    :type database_uri: str.
    """

    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def of_id(self, raid_id: int) -> Outlaw:
        """Method of_id searches for an Raid matching raid_id
        :param raid_id: Id of the Raid to be returned.
        :type raid_id: Integer.
        :returns: Raid -- The Raid matching raid_id.
        """
        # FIXME(tripledes)
        # Use GangFactory and OutlawFactory for both gang and members.
        query = raid_table.select().where(raid_table.c.id == raid_id)
        result = self.__connection.execute(query)
        members = self.__split_outlaws_ids(result.get('members'))
        outlaws = self.__create_outlaws_from_ids(members)
        #gang = GangFactory.create()
        return RaidFactory.create(
            id=result.get('id'),
            name=result.get('name'),
            outlaws=outlaws,
            sheriff=result.get('sheriff_id'),
            gang=result.get('gang_id'),
            date=result.get('date'))

    def add(self, new_outlaw: Outlaw) -> NoReturn:
        """Method add persists a new Outlaw to MySQL.
        :param new_outlaw: Object with the Outlaw information
        :type new_outlaw: Outlaw.
        :return: NoReturn.
        """
        outlaws_ids = self.__find_outlaws_ids()
        query = raid_table.insert().values(
            sheriff_id=new_raid.sheriff.id,
            gang_id=new_raid.gang.id,
            name=new_raid.name,
            members=outlaws_ids,
        )
        self.__connection.execute(query)

    def __join_bandidos_ids(self):
        ids = [bandido.id for bandido in self.bandidos]
        return ','.join(ids)

    def __split_outlaws_ids(self, outlaws: str) -> List[int]:
        ids = outlaws.split(',')
        return [int(id) for id in ids]

    def __create_outlaws_from_ids(self, members: list) -> List[Outlaw]:
        #results = list()
        #for member in members:
        #    results.append(
        #        OutlawFactory.create(
        #        )
        #    )
        pass
