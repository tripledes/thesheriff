import uuid

from thesheriff.domain.bandido.bandido import Bandido


class BandidoFactory(Bandido):
    
    @staticmethod
    def crear(name, correo) -> Bandido:
        return Bandido(None, name, correo)
