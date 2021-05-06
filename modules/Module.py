class Module:
	def __init__(self):
		self.OutputLogger=""
	
	def PrintOutput(self):
		print(f"{self.OutputLogger}")

	def SetData(self, data:str):
		if data:
			self.OutputLogger=data
				
	def AddData(self, data:str):
		if data:
			self.OutputLogger+=data