import string


class Mail:
    def __init__(self):
        sender = ""
        receiver = ""
        content = ""

    def mail_invite_friend(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.content = "Hello dear " + str(receiver) + "!\n " \
                       "Do you want to join this awesome game?" + \
                       "Come on!"

        if sender is None:
            raise Exception('User address needed to send an invitation')
        if receiver is None:
            raise Exception('Destination address needed to send an invitation')

    def send_notification_raid(self):
        return
