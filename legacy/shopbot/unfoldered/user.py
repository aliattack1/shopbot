class User:
	users = {}
	def __init__(self, telegram_id):
		if telegram_id in self.users.keys():
			pass
		self.id = telegram_id
		self.state = 'start'
		self.all_messages = []
		self.state_messages = []
		self.users[telegram_id]=self
		
	def reset(self):
		self.state = 'none'
		self.state_messages = []
	
	def tostate(self, state):
		self.state = state
		self.state_messages = []