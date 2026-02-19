import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = "7078547195:AAEJGnfgdabtfp4diTL0JtY8_ayoIm3r89I"

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

database = {}

# 1️⃣ Define States
class Registration(StatesGroup):
    name = State()
    family = State()
    phone = State()
    address = State()
    email = State()
    age = State()





# 2️⃣ Start Conversation
@dp.message(Command("register"))
async def register_start(message: Message, state: FSMContext):
    await message.answer("What is your name?")
    await state.set_state(Registration.name)


# 3️⃣ Handle Name
@dp.message(Registration.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("what is your family name?")
    await state.set_state(Registration.family)


@dp.message(Registration.family)
async def process_family(message: Message, state:FSMContext):
    await state.update_data(family=message.text)
    await message.answer("How old are you?")
    await state.set_state(Registration.phone)


@dp.message(Registration.phone)
async def process_phone(message: Message, state:FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("your phone number:")
    await state.set_state(Registration.address)


@dp.message(Registration.address)
async def process_address(message: Message, state:FSMContext):
    await state.update_data(address=message.text)
    await message.answer("your address:")
    await state.set_state(Registration.email)


@dp.message(Registration.email)
async def process_email(message: Message, state:FSMContext):
    await state.update_data(email=message.text)
    await message.answer("your email:")
    await state.set_state(Registration.age)

# 4️⃣ Handle Age
@dp.message(Registration.age)
async def process_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)

    data = await state.get_data()
    name = data["name"]
    family = data["family"]
    phone = data["phone"]
    address = data["address"]
    email = data["email"]
    age = data["age"]


    await message.answer(f"Registration complete!\nName: {name}\nFamily: {family}\n phone:{phone}\naddress: {address}\n email: {email}\nAge: {age}")

    await state.clear()  # Exit FSM


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
