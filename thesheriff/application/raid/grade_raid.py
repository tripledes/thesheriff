import inject

from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from thesheriff.domain.raid.repository.raid_repository import RaidRepository


class GradeRaid:
    """Class GradeRaid implements the Grade Raids use case.

    :param outlaw_repository: Repository managing Outlaw domain entities.
    :type outlaw_repository: OutlawRepository
    """

    @inject.autoparams()
    def __init__(self, raid_repository: RaidRepository,
                 outlaw_repository: OutlawRepository):
        self.__raid_repository = raid_repository
        self.__outlaw_repository = outlaw_repository

    def execute(self, raid_id: int) -> float:
        """execute is the actual action of the Grade a Raid use case.

        :param raid_id: Id of Raid entity to be graded.
        :type raid_id: Raid id
        :return: The raid grade.
        :rtype: Float
        """
        raid = self.__raid_repository.of_id(raid_id=raid_id)

        grade = 0.0
        total = 0.0
        divider = float(len(raid.rates))
        if divider > 0.0:
            for rate in raid.rates:
                total += rate

            grade = total / divider
            raid.sheriff.update_score(grade)

            # FIXME update sheriff score on db
            # self.__outlaw_repository.update(raid.sheriff)

        return grade
