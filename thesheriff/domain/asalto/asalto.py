from thesheriff.domain.bandido.sheriff import Sheriff
from thesheriff.domain.bandido.bandido import Bandido


class Asalto:

    def __init__(self, _id: int, name: str, bandidos: [Bandido], sheriff: Sheriff):
        self.bandidos = bandidos
        self.notas = []
        self.name = name
        self.id = _id
        self.sheriff = sheriff

    def nueva_puntuacion(self, nota):
        self.notas.append(nota)
