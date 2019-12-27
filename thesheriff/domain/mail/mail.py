from typing import NoReturn


class Mail:
    """Class Mail implements all contents for email notifications.
    """
    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def mail_invite_friend(self, sender: str, receiver: str) -> NoReturn:
        """Method mail_invite_friend builds the email body for sending
        invitations to join The Sheriff.

        :param sender: FROM address on the email.
        :type sender: String
        :param receiver: TO address on the email.
        :type receiver: String
        """
        self.__sender = sender
        self.__receiver = receiver
        self.__content = "Hello dear " + str(receiver) + "!\n " \
            "Do you want to join this awesome game?" + \
            "Come on!"

        if not self.__sender:
            raise Exception('User address needed to send an invitation')
        if not self.__receiver:
            raise Exception('Destination address needed to send an invitation')

    def send_notification_raid(self):
        return
