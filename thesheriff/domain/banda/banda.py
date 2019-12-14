import string
from typing import NoReturn

from thesheriff.domain.bandido.bandido import Bandido


class Banda:
    def __init__(self, nombre: string):
        self.nombre = nombre
        self.miembros = []
        self.asaltos_creados = 0
        self.id = -1

        if nombre is None:
            raise Exception('Nombre requerido')

    def miembros(self) -> [Bandido]:
        return self.miembros

    def add_miembros(self, miembros: [Bandido]) -> NoReturn:
        self.miembros = miembros
