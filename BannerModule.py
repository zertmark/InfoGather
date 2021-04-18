from pyfiglet import Figlet


class Banner(Figlet):
    def __init__(self):
        super().__init__()

    def GetBanner(self) -> str:
        return self.renderText("InfoGather")
