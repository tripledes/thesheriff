NUMERO_CRITERIOS = 4


class Puntuacion:
    """Puntuacion implements the score type for Asaltos.
    :param cantidad_comida: score for the amount of food
    :type cantidad_comida: float.
    :param calidad_comida: score for the quality of food
    :type calidad_comida: float.
    :param servicio: score for the service
    :type cantidad_comida: float.
    :param precio: score for the price
    :type precio: float.
    :return: Puntuacion.
    """

    def __init__(
            self, cantidad_comida: float, calidad_comida: float,
            servicio: float, precio: float
    ):
        self.cantidad_comida = cantidad_comida
        self.calidad_comida = calidad_comida
        self.servicio = servicio
        self.precio = precio

    def value(self) -> float:
        """value calculates the average score for an Asalto.
        :return: float.
        """
        return (
                       self.cantidad_comida + self.calidad_comida + self.servicio +
                       self.precio
               ) / NUMERO_CRITERIOS
