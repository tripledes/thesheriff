from typing import Optional, List
from thesheriff.domain.outlaw.outlaw import Outlaw


class OutlawFactory(Outlaw):
    """Class OutlawFactory produces Outlaws.
    """

    @staticmethod
    def create(name: str, email: str, id: Optional[int] = None) -> Outlaw:
        """Method create, produces an Outlaw instance.

        :param name: Outlaw's given name.
        :type name: String
        :param email: Outlaw's email.
        :type email: String
        :param id: Outlaw's id (optional)
        :type id: Optional[int]
        :return: The produced Outlaw.
        :rtype: Outlaw
        """
        return Outlaw(name, email, id)
