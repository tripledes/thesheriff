class Bandido:
    def __init__(self, id, name, correo):
        self.asaltos = []
        self.amigos = []
        self.bandas = []
        self.puntos = 0
        self.name = name
        self.id = id
        self.correo = correo

    def unirse_a_banda(self, banda):
        self.bandas.push(banda)
