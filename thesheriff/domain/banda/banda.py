import string


class Banda:
    def __init__(self, nombre: string):
        self.nombre = nombre
        miembros = []
        asaltos_creados = 0
        id = -1

        if nombre is None:
            raise Exception('Nombre requerido')
