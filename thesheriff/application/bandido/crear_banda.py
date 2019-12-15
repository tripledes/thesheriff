import inject

from thesheriff.domain.banda.banda_factory import BandaFactory
from thesheriff.domain.banda.repository.banda_repository import BandaRepository
from thesheriff.domain.banda.banda import Banda


class CrearBanda:

    @inject.autoparams()
    def __init__(self, banda_repository: BandaRepository):
        self.banda_repository = banda_repository

    def execute(self, nombre) -> Banda:
        banda = BandaFactory.crear(nombre)
        self.banda_repository.add(banda)
        return banda
