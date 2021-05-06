#TODO
import requests
class Avito:
	websites={
	"AviFinder":"https://avifinder.ru/?s=%2B{}"
	}
	@staticmethod
	def GetInfoAboutPhoneNumber(phone: str):
		return requests.get(Avito.websites["AviFinder"].format(phone))    	
