import string
from typing import Optional



class Banda:
    def __init__(self, nombre : string):
        self.nombre = nombre
        miembros = []
        asaltosCreados = 0
        id = 0

        if nombre is None:
            raise Exception('Nombre requerido')
