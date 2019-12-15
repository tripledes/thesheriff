import inject

from thesheriff.domain.banda.banda import Banda
from thesheriff.domain.banda.repository.banda_repository import BandaRepository


class ListarBandas:

    @inject.autoparams()
    def __init__(self, banda_repository: BandaRepository):
        self.banda_repository = banda_repository

    def execute(self, bandido_id: int) -> [Banda]:
        """execute is the actual action of the ListarBandas use case.
        :param bandido_id: ID of the Bandido performing the action.
        :type bandido_id: int.
        :return: Banda list.
        """

        bandas = []
        todas_las_bandas = self.banda_repository.all()

        for banda in todas_las_bandas:
            for bandido in banda.miembros:
                if bandido_id == bandido.id:
                    bandas.append(banda)

        return bandas
