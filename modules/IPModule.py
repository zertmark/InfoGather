from .ParsersInfo.IPParser import IPParser


class IPModule:
    def __init__(self, ip: str):
        self.IP = ip
        self.Parser = IPParser(self.IP)
        self.OutputLogger=""

    def CleanData(self, data: dict) -> dict:
        list_to_delete = ["status", "zip", "query", "region", "countryCode"]
        for key_to_delete in list_to_delete:
            del data[key_to_delete]     
        return data

    def IsExists(self, data: dict) -> bool:
        if data and data["status"] != "fail":
            return True
        return False

    def PrintOutput(self):
        print(f"{self.OutputLogger}")
    
    def SetData(self, data:str):
        if data:
            self.OutputLogger=data
    
    def AddData(self, data:str):
        if data:
            self.OutputLogger+=data

    def AddCleanedDataToOutput(self):
        for key in self.CleanData(self.Parser.GetData()):
            self.OutputLogger+=f"    [+] {key}: {self.Parser.GetData()[key]}\n"
        
    def Run(self):
        if self.IP:
            self.Parser.ParseIP()
            if self.IsExists(self.Parser.GetData()):
                self.SetData(f"[+] {self.IP} exists\n[+] Gathering info from IP address...\n")
                self.AddCleanedDataToOutput()
                self.PrintOutput()

            else:
                print(
                    f"[-] {self.IP} Doesn't exsist\nSkipping IP address info gathering...\n"
                )
