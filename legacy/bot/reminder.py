from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import os

# Replace with your actual bot token
BOT_TOKEN = "7078547195:AAEJGnfgdabtfp4diTL0JtY8_ayoIm3r89I"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("👋 Hello! This is a starter Aiogram bot.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
