from thesheriff.domain.asalto import Asalto
from thesheriff.domain.asalto.repository.asalto_repository import AsaltoRepository


class AsaltoMockRepository(AsaltoRepository):
    def of_id(self, asalto_id: int) -> Asalto:
        return self.asalto

    def add(self, asalto: Asalto):
        self.asalto = asalto

    def update(self, asalto: Asalto):
        self.asalto = asalto
