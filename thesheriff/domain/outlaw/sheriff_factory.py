from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.sheriff import Sheriff


class SheriffFactory(Sheriff):
    """Class SheriffFactory produces Sheriffs.
    """

    @staticmethod
    def create(outlaw: Outlaw) -> Sheriff:
        """Method create, produces an Sheriff instance.

        :param outlaw: Outlaw instance
        :type outlaw: Outlaw
        """
        return Sheriff(outlaw.name, outlaw.email, outlaw.id)
