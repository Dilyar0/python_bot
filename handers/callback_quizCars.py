from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_instance import bot

async def car_select_2(call: types.Message):
    photo = open("/media/cars/Mark2.jpeg", "rd")
    question = "what kind of car is this"
    answers = ["BMW f90", "TOYOTA mark 2 jzx100", "TOYOTA mark 2 jzx90", "TOYOTA supra"]
    markup = InlineKeyboardMarkup()
    button_car = InlineKeyboardButton("Следующий", callback_data="button_car_selected_2")
    markup.add(button_car)
    await bot.send_photo(call.chat.id, photo=photo)
    await bot.send_poll(
        call.chat.id,
        question=question,
        options=answers,
        correct_option_id=1,
        reply_markup=markup
    )

async def car_select_3(call: types.Message):
    photo = open("/media/cars/toyota_altezza.jpg", "rd")
    question = "what kind of car is this"
    answers = ["BMW X5", "TOYOTA chaser", "TOYOTA altezza", "MERSEDES e220"]
    markup = InlineKeyboardMarkup()
    button_car2 = InlineKeyboardButton("Следующий", callback_data="button_car_selected_3")
    markup.add(button_car2)
    await bot.send_photo(call.chat.id, photo=photo)
    await bot.send_poll(
        call.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=2,
        reply_markup=markup
    )

async def car_select_4(call: types.Message):
    photo = open("/media/cars/toyota_supra.jpg", "rd")
    question = "what kind of car is this"
    answers = ["FERRARY 625", "TOYOTA aristo", "HONDA accord", "TOYOTA supra"]
    await bot.send_photo(call.chat.id, photo=photo)
    await bot.send_poll(
        call.chat.id,
        question=question,
        options=answers,
        correct_option_id=3,

    )



def register_handlers_callback_homeWork(dp: Dispatcher):
    dp.register_callback_query_handler(car_select_2, lambda fun: fun.data == "button_car_selected_2")
    dp.register_callback_query_handler(car_select_3, lambda fun: fun.data == "button_car_selected_3")
    dp.register_callback_query_handler(car_select_4, lambda fun: fun.data == "button_car_selected_4")
