import asyncio
from bot import TOKEN_API
from aiogram import Bot , Dispatcher , Router , types
from aiogram.filters import CommandStart

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(msg:types.Message)-> None:
    await msg.answer(
        text="hello world"
    )
    

# a methode ......
async def main() -> None:
    bot = Bot(TOKEN_API)
     
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
    

