from thesheriff.domain.bandido.sheriff import Sheriff


class Asalto:

    def __init__(self, id, name, bandidos, sheriff: Sheriff):
        self.bandidos = bandidos
        self.notas = []
        self.name = name
        self.id = id
        self.sheriff = sheriff

    def nuevaPuntuacion(self, nota):
        self.notas.append(nota)
