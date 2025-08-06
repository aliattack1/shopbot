'''
from aiogram import Bot
import asyncio

async def delete_webhook():
    bot = Bot(token="7078547195:AAEJGnfgdabtfp4diTL0JtY8_ayoIm3r89I")
    await bot.delete_webhook(drop_pending_updates=True)
    print("Webhook deleted")

asyncio.run(delete_webhook())
'''
from core.request import Request
r = Request(1, '7078547195:AAEJGnfgdabtfp4diTL0JtY8_ayoIm3r89I', ['start'], {'start':'welcome to telenetshop'})
b = r.process()

