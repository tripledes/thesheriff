from thesheriff.domain.outlaw.outlaw import Outlaw
from typing import NoReturn


class Sheriff(Outlaw):
    def update_score(self, score: float) -> NoReturn:
        """Method update_score updates the Sheriff's score.

        :param score: New score to be added up.
        :type score: Float
        :return: No returned value.
        :rtype: NoReturn.
        """
        self.score += score

    def get_score(self) -> float:
        """Method get_score access to the current Sheriff's score.

        :return: The current score.
        :rtype: Float
        """
        return self.score
