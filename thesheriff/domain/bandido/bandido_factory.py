from thesheriff.domain.bandido.bandido import Bandido

class BandidoFactory(Bandido):
    
    @staticmethod
    def crear(self, id, name) -> Bandido:
        return Bandido(id, name)