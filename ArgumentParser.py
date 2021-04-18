import argparse


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="InfoGather by Zertmark",
                         prog="InfoGather")
        self.ArgumentsGroup = self.add_argument_group("Commands & arguments")

    def AddArguments(self):
        self.ArgumentsGroup.add_argument("-p",
                                         "--phone",
                                         help="A vicim's phone number",
                                         default="")

        self.ArgumentsGroup.add_argument("-c",
                                         "--country",
                                         help="A vicim's country",
                                         default="")

        self.ArgumentsGroup.add_argument("-e",
                                         "--email",
                                         help="A vicim's email",
                                         default="")

        self.ArgumentsGroup.add_argument("-i",
                                         "--ip",
                                         help="A vicim's IP address",
                                         default="")

    def ParseArguments(self):
        self.ArgumentsList = self.parse_args()

    def GetPhoneNumber(self) -> str:
        return self.ArgumentsList.phone

    def GetEmail(self) -> str:
        return self.ArgumentsList.email

    def GetIP(self) -> str:
        return self.ArgumentsList.ip

    def GetCountry(self) -> str:
        return self.ArgumentsList.country
