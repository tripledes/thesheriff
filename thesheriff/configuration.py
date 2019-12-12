import os

import inject
from flask import Flask

from thesheriff.domain.banda.repository.banda_repository import BandaRepository
from thesheriff.domain.bandido import BandidoRepository
from thesheriff.infrastructure import BandidoMySQLRepository
from thesheriff.infrastructure.repositoy.mysql_asalto_repository import AsaltoMySQLRepository
from thesheriff.domain.asalto.repository.asalto_repository import AsaltoRepository
from thesheriff.infrastructure.repositoy.mysql_banda_repository import BandaMySQLRepository

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
        binder.bind(BandidoRepository, BandidoMySQLRepository(
            application.config['DATABASE_URI']))
    inject.configure(config)
