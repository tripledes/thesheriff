from typing import NoReturn

from thesheriff.domain.mail.mail import Mail
from thesheriff.domain.raid.raid import Raid


class MailFactory:
    """Class Mail implements all contents for email notifications.
    """

    APPLICATION_MAIL = "thesheriff321123@gmail.com"

    @staticmethod
    def mail_invite_friend(sender: str, receiver: str) -> Mail:
        """Method mail_invite_friend builds the email body for sending
        invitations to join The Sheriff.

        :param sender: FROM address on the email.
        :type sender: String
        :param receiver: TO address on the email.
        :type receiver: String
        """
        if not sender:
            raise Exception('User address needed to send an invitation')
        if not receiver:
            raise Exception('Destination address needed to send an invitation')

        content = "Hello dear " + str(receiver) + "!\n " \
            "Do you want to join this awesome game?" + \
            "Come on!"

        return Mail(sender=sender, receiver=receiver, content=content)

    @staticmethod
    def mail_raid_finished(raid: Raid, raid_score: int) -> Mail:
        """Method mail_invite_friend builds the email body for sending
        invitations to join The Sheriff.

        :param raid: The last finished raid.
        :type raid: Raid
        :param raid_score: Sheriff score on the raid.
        :type raid_score: int
        """

        content = "Hello Sheriff " + str(raid.sheriff.name) + "!\n\n" \
            "Here is your updated score after the raid was finished: \n" + \
            "Raid: " + str(raid.name) + "\n" +\
            "Sheriff score on raid: " + str(raid_score) + "\n" +\
            "Gang updated score: " + str(raid.gang.score())

        return Mail(sender=MailFactory.APPLICATION_MAIL,
                    receiver=raid.sheriff.email, content=content)
