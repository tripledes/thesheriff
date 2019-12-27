class Score:
    """Score implements the score type for Raids.

    :param food_quantity: score for the amount of food
    :type food_quantity: float.
    :param food_quality: score for the quality of food
    :type food_quality: float.
    :param service_quality: score for the service
    :type service_quality: float.
    :param price: score for the price
    :type price: float.
    """

    def __init__(
            self, food_quantity: float, food_quality: float,
            service_quality: float, price: float
    ):
        self.__food_quantity = food_quantity
        self.__food_quality = food_quality
        self.__service_quality = service_quality
        self.__price = price
        self.__criterias = 4

    def value(self) -> float:
        """value calculates the average score for a Raid.

        :return: The actual score.
        :rtype: Float
        """
        return (
            self.__food_quantity + self.__food_quality +
            self.__service_quality + self.__price
        ) / self.__criterias
