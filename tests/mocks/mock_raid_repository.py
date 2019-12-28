from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.raid.repository.raid_repository import RaidRepository
from typing import List


class MockRaidRepository(RaidRepository):
    def of_id(self, raid_id: int) -> Raid:
        return self.raid

    def add(self, raid: Raid):
        self.raid = raid
        return raid

    def update(self, raid: Raid):
        self.raid = raid

    def update_rates(self, raid: Raid):
        pass
