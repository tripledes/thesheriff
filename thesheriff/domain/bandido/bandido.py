class Bandido:
    def __init__(self, _id, name, correo):
        self.asaltos = []
        self.amigos = []
        self.bandas = []
        self.puntos = 0
        self.name = name
        self.id = _id
        self.correo = correo

    def unirse_a_banda(self, banda):
        self.bandas.append(banda)
