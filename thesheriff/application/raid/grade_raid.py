from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository


class GradeRaid:
    """Class GradeRaid implements the Grade Raids use case.

    :param outlaw_repository: Repository managing Outlaw domain entities.
    :type outlaw_repository: OutlawRepository
    """

    def __init__(self, outlaw_repository: OutlawRepository):
        self.__outlaw_repository = outlaw_repository

    def execute(self, raid: Raid) -> float:
        """execute is the actual action of the Grade a Raid use case.

        :param raid: The Raid entity to be graded.
        :type raid: Raid
        :return: The raid grade.
        :rtype: Float
        """
        grade = 0
        total = 0
        divider = len(raid.rates)
        if divider > 0:
            for rate in raid.rates:
                total += rate

            grade = total / divider
            raid.sheriff.update_score(grade)
            self.__outlaw_repository.update(raid.sheriff)

        return grade
