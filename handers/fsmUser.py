from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_instance import dp, bot
from database import user_db


class FSMUSER(StatesGroup):
    id = State()
    user_name = State()
    firstName = State()
    lastName = State()



async def greeteng_user(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_start_register = InlineKeyboardButton("continue", callback_data="user_id")
    markup.add(button_start_register)
    await bot.send_message(message.from_user.id, f"welcome, {message.from_user.first_name}\nclick on the button to continue", reply_markup=markup)


async def user_id(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = call.message.from_user.id
    await FSMUSER.next()
    await call.message.reply("Send me your user name")


async def user_name(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["user_name"] = call.from_user.first_name
    await FSMUSER.next()
    await call.message.reply("Your first first name?")


async def first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["first_name"] = message.text
    await FSMUSER.next()
    await message.reply("Last name?")


async def last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["last_name"] = message.from_user.last_name
    await user_db.sql_command_insert(state)
    await state.finish()


def register_handler_fsmuser(dp: Dispatcher):
    dp.register_message_handler(greeteng_user, commands=["start_register"])
    dp.register_callback_query_handler(user_id, lambda fun: fun.data == "user_id")
    dp.register_message_handler(user_name, commands=["user_user"])
    dp.register_message_handler(first_name, commands=["first_name"])
    dp.register_message_handler(last_name, commands=["last_name"])