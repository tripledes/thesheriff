from thesheriff.domain.asalto.asalto import Asalto


class AsaltoFactory(Asalto):

    @staticmethod
    def crear(_id, name, bandidos, sheriff) -> Asalto:
        return Asalto(_id, name, bandidos, sheriff)
