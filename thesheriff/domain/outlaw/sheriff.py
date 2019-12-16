from typing import NoReturn
from thesheriff.domain.outlaw.outlaw import Outlaw


class Sheriff(Outlaw):
    def __init__(self, outlaw: Outlaw):
        super().__init__(outlaw.id, outlaw.name, outlaw.email)
        self.__outlaw = outlaw

    def update_score(self, score) -> NoReturn:
        self.__outlaw.score += score

    def get_score(self) -> float:
        return self.__outlaw.score
