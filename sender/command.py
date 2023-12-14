from sender.commandinterface import CommandInterface


class Command(CommandInterface):
    def __init__(self):
        super().__init__()

    def execute(self, uid: str):
        """ Execute the mailing process"""
        self.emailer.make_csv(uid)

    def status(self, uid: str) -> bool:
        """checks the whether the mail has been sent"""

        data = self.model.find(uid)
        if data['status']:
            return True
        else:
           return False

    # def reverse(self, uid):
    #     pass

    def insert(self, args):
        self.model.insert(args)

