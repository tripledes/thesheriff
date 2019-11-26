from thesheriff.domain.banda.banda import Banda

class BandaFactory(Banda):

    @staticmethod
    def crear(self, id, name) -> Banda:
        return Banda(id, name)