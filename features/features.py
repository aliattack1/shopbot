class Features:
	@staticmethod
	def getfeature(name):
		if name == 'start':
			from features.startfeature import Startfeature
			return Startfeature