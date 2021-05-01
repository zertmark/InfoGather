from .ParsersInfo.Avito import Avito
from .ParsersInfo.Facebook import Facebook
from .ParsersInfo.VK import VK
from .ParsersInfo.WhatsUp import WhatsUp
from .ParsersInfo.PhoneConverter import PhoneConverter

#COLOR='\033[32m'
#STYLE='\033[1m'
#RESET='\033[0m'
class PhoneModule:
    def __init__(self, phone: str, country=""):
        self.PhoneNumber = phone
        self.Country = country
        self.OutputLogger=""
        if self.PhoneNumber:
            self.PhoneConverter = PhoneConverter(phone, country)

    def setPhoneNumber(self, new_phone_number: str):
        if new_phone_number:
            self.PhoneNumber = new_phone_number
    
    def PrintOutput(self):
        print(f"{self.OutputLogger}")

    def Run(self):
        if self.PhoneNumber:
            if self.PhoneConverter.IsPhoneNumberExists():
                self.setPhoneNumber(
                    self.PhoneConverter.GetConvertedPhoneNumber())

                self.OutputLogger+=f"[+] {self.PhoneNumber} exists\nGathering info...\n[+] Country code: {self.PhoneConverter.GetCountryCode()}"
                self.PrintOutput()
            else:
                print(f"[-] {self.PhoneNumber} doesn't exist\nSkipping phone number info gathering...\n")
