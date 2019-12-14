EMPTY_ARRAY = []
INIT_ZERO = 0
NUM_ATRIBUTES_TO_LIST = 4


class Bandido:

    def __init__(self, _id: int, name: str, correo: str):
        self.asaltos = EMPTY_ARRAY
        self.amigos = EMPTY_ARRAY
        self.bandas = EMPTY_ARRAY
        self.puntos = INIT_ZERO
        self.name = name
        self.id = _id
        self.correo = correo

    def unirse_a_banda(self, banda):
        self.bandas.append(banda)

    def lista_amigos(self):
        return self.amigos
