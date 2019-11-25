import abc

class AsaltoRepository(abc.ABC):

    @abc.abstractmethod
    def of_id(self):
        pass

    @abc.abstractmethod
    def add(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass