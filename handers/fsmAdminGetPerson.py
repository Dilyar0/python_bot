from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot_instance import dp, bot


class FSMADMIN(StatesGroup):
    id = State()
    user_name = State()
    firstName = State()
    lastName = State()


async def is_user_id(message: types.Message):
    global USER_ID
    USER_ID = message.from_user.id
    await bot.send_message(message.from_user.id, f"welcome, {message.from_user.first_name}")


async def user_start(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == USER_ID:
        async with state.proxy() as data:
            data["name"] = message.text
        await FSMADMIN.next()
        await message.reply("Your name?")


async def first_name(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == USER_ID:
        async with state.proxy() as data:
            data["last name"] = message.text
        await FSMADMIN.next()
        await message.reply("Last name?")


async def last_name(message: types.Message,
                           state: FSMContext):
    if message.from_user.id == USER_ID:
        async with state.proxy() as data:
            data["last_name"] = message.text
        async with state.proxy() as data:
            await message.reply(str(data))
        await state.finish()


def register_handler_fsmAdminGetPerson(dp: Dispatcher):
    dp.register_message_handler(is_user_id, commands=["user"])
    dp.register_message_handler(user_start, commands=["getStarted"])
    dp.register_message_handler(first_name, commands=["first_name"])
    dp.register_message_handler(last_name, commands=["last_name"])
