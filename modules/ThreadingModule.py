from threading import Thread
class Thread(Thread):
	def __init__(self, Parser:object):
		super().__init__()
		self.Parser=Parser

	def run(self):
		self.Parser.Run()
		
