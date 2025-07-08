from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio
from features.features import Features
class Botl:
	def __init__(self, id, token, features, messages):
		self.id = id
		self.token = token
		self.messages = messages
		self.state = ''
		self.context = {}
		self.commandhandlers = {}
		self.bot = Bot(token=token)
		self.dp = Dispatcher()

		
		for feature in features:
			self.installfeature(feature)
		asyncio.run(self.pol())
	async def pol(self):
		await self.dp.start_polling(self.bot)
	def installfeature(self, feature):
		props = Features.getfeature(feature).get_install_props(self.messages)
		if props[0][0] == '/':
			@self.dp.message(Command(props[0][1:]))
			async def _(message:Message):
				await message.answer(props[1]())
		self.commandhandlers[props[0]] = props[1]