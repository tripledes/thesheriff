class Asalto:

    def __init__(self, id, name, bandidos, sheriff):
        self.bandidos = bandidos
        self.scores = []
        self.name = name
        self.id = id
        self.sheriff = sheriff

    def puntuar(self, score):
        self.scores.append(score)
