import os

import inject
from flask import Flask

from thesheriff.infrastructure.asalto.asalto_mysql_repository import AsaltoMySQLRepository
from thesheriff.infrastructure.asalto.banda_mysql_repository import BandaMySQLRepository
from thesheriff.infrastructure.asalto.bandido_mysql_repository import BandidoMySQLRepository
from thesheriff.domain.asalto.asalto_repository import AsaltoRepository
from thesheriff.domain.asalto.banda_repository import BandaRepository
from thesheriff.domain.asalto.bandido_repository import BandidoRepository


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(AsaltoRepository, AsaltoMySQLRepository(
            application.config['DATABASE_URI']))
        binder.bind(BandaRepository, BandaMySQLRepository(
            application.config['DATABASE_URI']))
        binder.bind(BandidoRepository, AsaltoMySQLRepository(
            application.config['DATABASE_URI']))
    inject.configure(config)
