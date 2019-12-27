import inject
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from thesheriff.domain.outlaw.outlaw_factory import OutlawFactory
from thesheriff.application.outlaw.request.create_outlaw_request import \
    CreateOutlawRequest


class CreateOutlaw:
    """Class CreateOutlaw implements the Outlaw creation use case.

    :param outlaw_repository: Repository managing Outlaw domain entities.
    :type outlaw_repository: OutlawRepository
    """

    @inject.autoparams()
    def __init__(self, outlaw_repository: OutlawRepository):
        self.__outlaw_repository = outlaw_repository

    def execute(self, request: CreateOutlawRequest) -> Outlaw:
        """execute is the actual action of the Create Outlaw use case.

        :param request: Request holding the new Outlaw details.
        :type request: CreateOutlawRequest
        :return: The newly created Outlaw.
        :rtype: Outlaw
        """
        new_outlaw = OutlawFactory.create(request.name, request.email)
        self.__outlaw_repository.add(new_outlaw)
        return new_outlaw
