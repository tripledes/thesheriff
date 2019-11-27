class Puntuacion:
    def __init__(self, cantidadComida, calidadComida, servicio, precio):
        self.cantidadComida = cantidadComida
        self.calidadComida = calidadComida
        self.servicio = servicio
        self.precio = precio

    def value(self):
        return (self.cantidadComida + self.calidadComida + self.servicio + self.precio) / 4
