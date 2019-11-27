class Bandido:
    def __init__(self, id, name):
        self.asaltos = []
        self.amigos = []
        self.bandas = []
        self.score = 0
        self.name = name
        self.id = id

    def unirse_a_banda(self, banda):
        self.bandas.push(banda)
