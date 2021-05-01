from .ParsersInfo.EmailValidate import EmailValidater


class EmailModule:
    def __init__(self, email: str):
        self.Email = email
        self.OutputLogger=""

    def IsInDatabase(self) -> bool:
        pass

    def GetInfoFromDatabase(self) -> list:
        pass

    def CheckServices(self):
        pass

    def CheckForLeaks(self):
        pass

    def PrintOutput(self):
        print(f"{self.OutputLogger}")

    def Run(self):
        if self.Email:
            if EmailValidater.IsEmailExists(self.Email):
                self.OutputLogger+=f"[+] {self.Email} exists\nGathering info...\n"
                self.CheckForLeaks()
                self.CheckServices()
                self.PrintOutput()

            else:
                print(f"[-] {self.Email} doesn't exists\nSkipping email info gathering...\n")
