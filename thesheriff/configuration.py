import os

import inject
from flask import Flask
from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer,  MetaData, Table, Text
)
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from thesheriff.domain.mail.notifier.mail_notifier import MailNotifier
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from thesheriff.domain.raid.repository.raid_repository import RaidRepository
from thesheriff.infrastructure.repository.mysql_gang_repository import \
    MySQLGangRepository
from thesheriff.infrastructure.repository.mysql_outlaw_repository import \
    MySQLOutlawRepository
from thesheriff.infrastructure.repository.mysql_raid_repository import \
    MySQLRaidRepository
from thesheriff.infrastructure.notifier.smtp_mail_notifier import \
    SMTPMailNotifier

METADATA = MetaData()

outlaw_table = Table('outlaws', METADATA,
                     Column('id', Integer, primary_key=True,
                            autoincrement=True),
                     Column('name', Text, nullable=False),
                     Column('email', Text, nullable=False),
                     Column('score', Float, nullable=False, default=0.0),
                     Column('gangs', ForeignKey('gangs.id')),
                     Column('gangs_score', ForeignKey('gangs.id')))

gang_table = Table('gangs', METADATA,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('score', Integer, nullable=False, default=0.0),
                   Column('owner_id', Integer, nullable=False),
                   Column('name', Text, nullable=False),
                   Column('members', ForeignKey('outlaws.id')))

raid_table = Table('raids', METADATA,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('sheriff_id', Integer, nullable=False),
                   Column('gang_id', Integer, nullable=False),
                   Column('name', Text, nullable=False),
                   Column('location', Text, nullable=False),
                   Column('members', Text, nullable=False),
                   Column('rates', Text),
                   Column('date', DateTime, nullable=False))


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )
    application.config.update(
        METADATA=METADATA
    )
    application.config.update(
        GANG_TABLE=gang_table
    )
    application.config.update(
        OUTLAW_TABLE=outlaw_table
    )
    application.config.update(
        RAID_TABLE=raid_table
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(RaidRepository, MySQLRaidRepository(
            application.config['DATABASE_URI'],
            application.config['METADATA'],
            application.config['RAID_TABLE']))
        binder.bind(GangRepository, MySQLGangRepository(
            application.config['DATABASE_URI'],
            application.config['METADATA'],
            application.config['GANG_TABLE']))
        binder.bind(OutlawRepository, MySQLOutlawRepository(
            application.config['DATABASE_URI'],
            application.config['METADATA'],
            application.config['OUTLAW_TABLE']))
        binder.bind(MailNotifier, SMTPMailNotifier)

    inject.configure(config)
