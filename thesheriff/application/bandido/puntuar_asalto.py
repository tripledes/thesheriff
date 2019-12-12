"""
.. module:: puntuar_asalto
   :platform: Windows,Unix
   :synopsis: Puntuar Asalto use case
.. moduleauthor:: The Sheriff Team <thesheriff@team.net>
"""
from typing import NoReturn

import inject

from thesheriff.domain.asalto.repository.asalto_repository import AsaltoRepository
from thesheriff.domain.bandido.repository.bandido_repository import BandidoRepository
from thesheriff.domain.bandido.puntuacion import Puntuacion


class PuntuarAsalto:
    """PuntuarAsalto implements the rating Asalto use case.
    :param bandido_repository: Repository object for bandidos
    :type bandido_repository: BandidoRepository.
    :param asalto_repository: Repository object for asaltos
    :type asalto_repository: AsaltoRepository.
    """
    @inject.autoparams()
    def __init__(
        self, bandido_repository: BandidoRepository,
        asalto_repository: AsaltoRepository
    ):
        self.asalto_repository = asalto_repository
        self.bandido_repository = bandido_repository

    def execute(
        self, asalto_id: int, bandido_id: int, puntuacion: Puntuacion
    ) -> NoReturn:
        """execute is the actual action of the PuntuarAsalto use case.
        :param asalto_id: ID of the Asalto to be rated
        :type asalto_id: int.
        :param bandido_id: ID of the Bandido performing the action.
        :type bandido_id: int.
        :param puntuacion: Asalto's rate
        :type puntuacion: Puntuacion.
        :return: NoReturn.
        """
        bandido = self.bandido_repository.of_id(bandido_id)
        asalto = self.asalto_repository.of_id(asalto_id)

        if bandido:
            asalto.nueva_puntuacion(puntuacion.value())
            self.asalto_repository.update(asalto)
