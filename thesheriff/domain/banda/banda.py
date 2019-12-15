import string
from typing import NoReturn

from thesheriff.domain.bandido.bandido import Bandido


class Banda:
    def __init__(self, creador_id: int, nombre: str):
        self.nombre = nombre
        self.miembros = []
        self.asaltos_creados = 0
        self.creador_id = creador_id
        self.id = None

        if nombre is None:
            raise Exception('Nombre requerido')

    def miembros(self) -> [Bandido]:
        return self.miembros

    def add_miembros(self, miembros: [Bandido]) -> NoReturn:
        self.miembros = miembros
