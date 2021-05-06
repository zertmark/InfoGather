import requests



class IPParser:
    def __init__(self, IP: str):
        self.website = f'http://ip-api.com/json/{IP}'
        self.Data = None

    def ParseIP(self):
        self.Data = requests.get(self.website).json()

    def GetData(self):
        return self.Data
