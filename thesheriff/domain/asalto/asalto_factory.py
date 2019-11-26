from thesheriff.domain.asalto.asalto import Asalto

class AsaltoFactory(Asalto):
    
    @staticmethod
    def crear(self, id, name, bandidos, sheriff) -> Asalto:
        return Asalto(id, name, bandidos, sheriff)