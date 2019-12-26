from typing import Optional, List
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.gang.gang import Gang


class OutlawFactory(Outlaw):
    """Class OutlawFactory produces Outlaws.
    """

    @staticmethod
    def create(name: str, email: str, id: Optional[int] = None) -> Outlaw:
        """Method create, produces a Outlaw instance.

        :param name: Outlaw's given name.
        :type name: String
        :param email: Outlaw's email.
        :type email: String
        :return: The produced Outlaw.
        :rtype: Outlaw
        """
        return Outlaw(name, email, id)
