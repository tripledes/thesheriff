from typing import NoReturn, List

from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository


class MockOutlawRepository(OutlawRepository):

    def __init__(self):
        self.outlaw = None

    def of_id(self, outlaw_id) -> Outlaw:
        return self.outlaw

    def add(self, new_outlaw: Outlaw) -> int:
        self.outlaw = new_outlaw
        return 1

    def update(self, mod_outlaw: Outlaw) -> NoReturn:
        self.outlaw = mod_outlaw

    def remove(self, outlaw_id: int) -> NoReturn:
        self.outlaw = None

    def get_friends(self, outlaw_id: int) -> List[Outlaw]:
        outlaw_1 = Outlaw("Outlaw1", "b1@yopmail.com", 1)
        outlaw_2 = Outlaw("Outlaw2", "b2@yopmail.com", 2)
        outlaw_3 = Outlaw("Outlaw3", "b3@yopmail.com", 3)

        return [outlaw_1, outlaw_2, outlaw_3]

    def all(self) -> [Outlaw]:
        return [
            Outlaw("Outlaw1", "b1@yopmail.com", 1),
            Outlaw("Outlaw2", "b2@yopmail.com", 2),
            Outlaw("Outlaw3", "b3@yopmail.com", 3)
        ]
