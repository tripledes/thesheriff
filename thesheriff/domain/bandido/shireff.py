from thesheriff.domain.bandido.bandido import Bandido

class Sheriff(Bandido):
    def __init__(self, bandido):
        self.bandido = bandido
        self.score = 0

    def actualizarScore(self, score):
        self.score += score
