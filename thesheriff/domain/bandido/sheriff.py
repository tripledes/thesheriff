from thesheriff.domain.bandido.bandido import Bandido


class Sheriff(Bandido):
    def __init__(self, bandido):
        super().__init__(bandido.id, bandido.name, bandido.correo)
        self.bandido = bandido

    def actualizar_puntos(self, puntos):
        self.puntos += puntos

    def puntos(self):
        return self.bandido.puntos
