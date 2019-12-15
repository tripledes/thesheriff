from thesheriff.domain.banda.banda import Banda


class BandaFactory(Banda):

    @staticmethod
    def crear(creador_id: int, name: str) -> Banda:
        return Banda(creador_id, name)
