import inject

from thesheriff.domain.banda.banda_factory import BandaFactory
from thesheriff.domain.banda.banda_repository import BandaRepository


class CrearBanda:

    @inject.autoparams()
    def __init__(self, banda_repository: BandaRepository, banda_factory: BandaFactory):
        self.banda_repository = banda_repository
        self.banda_factory = banda_factory

    def execute(self, nombre):
        banda = self.banda_factory.crear(nombre)
        self.banda_repository.add(banda)
