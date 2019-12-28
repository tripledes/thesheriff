from typing import Optional, List
from thesheriff.domain.outlaw.outlaw import Outlaw


class OutlawFactory(Outlaw):
    """Class OutlawFactory produces Outlaws.
    """

    @staticmethod
    def create(
        name: str, email: str, outlaw_id: Optional[int] = None
    ) -> Outlaw:
        """Method create, produces an Outlaw instance.

        :param name: Outlaw's given name.
        :type name: String
        :param email: Outlaw's email.
        :type email: String
        :param outlaw_id: Optional, Outlaw's Id.
        :type outlaw_id: Integer
        :return: The produced Outlaw.
        :rtype: Outlaw
        """
        return Outlaw(name, email, outlaw_id)

    @staticmethod
    def create_with_id(outlaw_id: int) -> Outlaw:
        """Method create, produces a Outlaw instance with just its Id.

        :param outlaw_id: Outlaw's Id.
        :type outlaw_id: Integer
        :return: The created Outlaw.
        :rtype: Outlaw
        """
        return Outlaw(None, None, outlaw_id)
