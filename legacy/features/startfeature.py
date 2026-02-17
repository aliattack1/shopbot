def startmessage(startingmessage):
	return startingmessage


class Startfeature:
	@staticmethod
	def get_install_props(messages):
		trigger = '/start'
		callback = lambda: startmessage(messages['start'])
		return (trigger, callback)
		