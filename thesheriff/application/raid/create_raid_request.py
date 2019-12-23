from datetime import datetime


class CreateRaidRequest:
    def __init__(self,
                 name: str,
                 date: datetime,
                 location: str,
                 gang_id: str,
                 sheriff_id: int,
                 outlaw_ids: list
                 ):
        self.name = name
        self.date = date
        self.location = location
        self.gang_id = gang_id
        self.sheriff_id = sheriff_id
        self.outlaw_ids = outlaw_ids
