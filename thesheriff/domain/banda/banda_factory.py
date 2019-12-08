from thesheriff.domain.banda.banda import Banda

class BandaFactory(Banda):

    @staticmethod
    def crear(self, name) -> Banda:
        return Banda(name)