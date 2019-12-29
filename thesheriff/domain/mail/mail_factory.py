from typing import NoReturn

from thesheriff.domain.mail.mail import Mail
from thesheriff.domain.raid.raid import Raid


class MailFactory:
    """Class Mail implements all contents for email notifications.
    """

    APPLICATION_MAIL = "thesheriff321123@gmail.com"

    @staticmethod
    def mail_invite_friend(sender_mail: str, receiver_mail: str) -> Mail:
        """Method mail_invite_friend builds the email body for sending
        invitations to join The Sheriff.

        :param sender_mail: FROM address on the email.
        :type sender_mail: String
        :param receiver_mail: TO address on the email.
        :type receiver_mail: String
        """
        if not sender_mail:
            raise Exception('User address needed to send an invitation')
        if not receiver_mail:
            raise Exception('Destination address needed to send an invitation')

        content = "Hello dear " + str(receiver_mail) + "!\n " \
            "Do you want to join this awesome game?" + \
            "Come on!"

        return Mail(sender_mail, receiver_mail, content)

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
