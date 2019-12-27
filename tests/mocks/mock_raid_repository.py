from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.raid.repository.raid_repository import RaidRepository


class MockRaidRepository(RaidRepository):
    def __init__(self):
        self.__raid = None

    def of_id(self, raid_id: int) -> Raid:
        return self.__raid

    def add(self, raid: Raid) -> Raid:
        self.__raid = raid
        return raid

    def update(self, raid: Raid):
        self.__raid = raid

    def update_rates(self, raid: Raid):
        self.__raid.rates = raid.rates
