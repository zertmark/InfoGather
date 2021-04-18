from modules.BannerModule import Banner
from modules.ArgumentParser import ArgumentParser
from modules.PhoneModule import PhoneModule
from modules.EmailModule import EmailModule
from modules.IPModule import IPModule
from modules.ThreadingModule import Thread
from ctypes import windll

class Main:
    def __init__(self):
        self.Banner = Banner().GetBanner()
        self.Parser = ArgumentParser()
        self.Parser.AddArguments()
        self.Parser.ParseArguments()
        self.EnableColorOutput()
        self.ListParsers = [
            PhoneModule(self.Parser.GetPhoneNumber(),
                        self.Parser.GetCountry()),
            EmailModule(self.Parser.GetEmail()),
            IPModule(self.Parser.GetIP())
        ]

    def PrintBanner(self):
        print(self.Banner)

    def EnableColorOutput(self):
        windll.kernel32.SetConsoleMode(windll.kernel32.GetStdHandle(-11), 7)

    def CreateThreadsList(self):
    	self.ThreadsList=[]
    	for parser in self.ListParsers:
    		self.ThreadsList.append(Thread(parser))

    def Run(self):	
    	for thread in self.ThreadsList:
    		thread.start()



if __name__ == "__main__":
    main = Main()
    main.PrintBanner()
    main.CreateThreadsList()
    main.Run()
