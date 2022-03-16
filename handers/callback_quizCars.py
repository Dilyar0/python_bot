from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_instance import bot


async def car_select_2(call: types.CallbackQuery):
    photo = open("media/cars/Mark2.jpg", "rb")
    question = "what kind of car is this"
    answers = ["BMW f90", "TOYOTA mark 2 jzx100", "TOYOTA mark 2 jzx90", "TOYOTA supra"]
    markup = InlineKeyboardMarkup()
    button_car = InlineKeyboardButton("Следующий", callback_data="button_car_selected_2")
    markup.add(button_car)
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=1,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup
    )


async def car_select_3(call: types.CallbackQuery):
    photo = open("media/cars/toyota_altezza.jpg", "rb")
    question = "what kind of car is this"
    answers = ["BMW X5", "TOYOTA chaser", "TOYOTA altezza", "MERSEDES e220"]
    markup = InlineKeyboardMarkup()
    button_car2 = InlineKeyboardButton("Следующий", callback_data="button_car_selected_3")
    markup.add(button_car2)
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=2,
        is_anonymous=False,
        type="quiz",
        reply_markup=markup
    )


async def car_select_4(call: types.CallbackQuery):
    photo = open("media/cars/toyota_supra.jpg", "rb")
    question = "what kind of car is this"
    answers = ["FERRARY 625", "TOYOTA aristo", "HONDA accord", "TOYOTA supra"]
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=3,
        is_anonymous=False,
        type="quiz"
    )


def register_handlers_callback_homeWork(dp: Dispatcher):
    dp.register_callback_query_handler(car_select_2, lambda fun: fun.data == "button_car_selected_1")
    dp.register_callback_query_handler(car_select_3, lambda fun: fun.data == "button_car_selected_2")
    dp.register_callback_query_handler(car_select_4, lambda fun: fun.data == "button_car_selected_3")
