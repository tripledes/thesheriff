from thesheriff.domain.bandido.bandido import Bandido

class Sheriff(Bandido):
    def __init__(self, bandido):
        self.bandido = bandido
        self.puntos = 0

    def actualizarPuntos(self, puntos):
        self.puntos += puntos

    def puntos(self):
        return self.puntos
