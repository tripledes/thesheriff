from typing import NoReturn

from thesheriff.domain.banda.banda import Banda
from thesheriff.domain.bandido import Bandido
from thesheriff.domain.bandido.sheriff import Sheriff
from thesheriff.domain.bandido.bandido import Bandido


class Asalto:

    def __init__(self, _id: int, name: str, bandidos: [Bandido], sheriff: Sheriff, banda: Banda):
        self.bandidos = bandidos
        self.notas = []
        self.name = name
        self.id = _id
        self.sheriff = sheriff
        self.banda = banda

    def nueva_puntuacion(self, nota) -> NoReturn:
        self.notas.append(nota)

    def puede_finalizar(self) -> bool:
        return len(self.notas) == len(self.bandidos)
