import abc
from thesheriff.domain.mail.mail import Mail


class MailNotifier(abc.ABC):
    """Interface MailNotifier, defines how all mail notifier
    implementations will behave.
    """

    @abc.abstractmethod
    def send(self, mail: Mail):
        pass
