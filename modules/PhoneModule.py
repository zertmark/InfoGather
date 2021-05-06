from .ParsersInfo.Avito import Avito
from .ParsersInfo.Facebook import Facebook
from .ParsersInfo.VK import VK
from .ParsersInfo.WhatsUp import WhatsUp
from .ParsersInfo.PhoneConverter import PhoneConverter
from .Module import Module
#COLOR='\033[32m'
#STYLE='\033[1m'
#RESET='\033[0m'
class PhoneModule(Module):
    def __init__(self, phone: str, country=""):
        self.PhoneNumber = phone
        self.Country = country
        self.OutputLogger=""
        if self.PhoneNumber:
            self.PhoneConverter = PhoneConverter(phone, country)

    def setPhoneNumber(self, new_phone_number: str):
        if new_phone_number:
            self.PhoneNumber = new_phone_number

    def Run(self):
        if self.PhoneNumber:
            if self.PhoneConverter.IsPhoneNumberExists():
                self.setPhoneNumber(
                    self.PhoneConverter.GetConvertedPhoneNumber())

                self.AddData(
                    f"[+] {self.PhoneNumber} exists\n[+] Gathering info...\n    [+] Country code: {self.PhoneConverter.GetCountryCode()}\n")
                self.AddData(str(Avito.GetInfoAboutPhoneNumber(self.PhoneNumber)))
                self.PrintOutput()
            else:
                print(f"[-] {self.PhoneNumber} doesn't exist\nSkipping phone number info gathering...\n")
