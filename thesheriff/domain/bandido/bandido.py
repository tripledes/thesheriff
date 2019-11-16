class Bandido:
    def __init__(self, id, name, score, bandas, amigos, asaltos):
        self.asaltos = asaltos
        self.amigos = amigos
        self.bandas = bandas
        self.score = score
        self.name = name
        self.id = id

    def unirse_a_banda(self, banda):
        self.bandas.push(banda)