from typing import NoReturn, Optional
from thesheriff.domain.outlaw.outlaw import Outlaw


class Sheriff(Outlaw):
    def update_score(self, score) -> NoReturn:
        self.score += score

    def get_score(self) -> float:
        return self.score
