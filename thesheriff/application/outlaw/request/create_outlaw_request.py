class CreateOutlawRequest:
    """Class CreateOutlawRequest holds data required to create an Outlaw.

    :param name: Outlaw's given name.
    :type name: String
    :param email: Outlaw's email.
    :type email: String
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
