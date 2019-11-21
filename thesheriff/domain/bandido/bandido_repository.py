import abc


class BandidoRepository(abc.ABC):
    @abc.abstractmethod
    def of_id(self):
        pass

    @abc.abstractmethod
    def add(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def remove(self):
        pass