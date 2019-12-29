class InviteFriendRequest:
    """Class InviteFriendRequest holds data required to invite an Outlaw's
        friend.

        :param outlaw_id: Outlaw's id.
        :type outlaw_id: int
        :param mail_address_receiver: friend's email
        :type mail_address_receiver: str
        """

    def __init__(self, outlaw_id: int, mail_address_receiver: str):
        self.outlaw_id = outlaw_id
        self.mail_address_receiver = mail_address_receiver
