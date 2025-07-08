from core.bot import Botl
class Request:
	def __init__(self, id, token, features, messages):
		self.id = id
		self.token = token
		self.features = features
		self.messages = messages
		
	def process(self):
		return Botl(self.id, self.token, self.features, self.messages)