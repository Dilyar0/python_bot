from aiogram import executor, types, bot
from bot_instance import dp
from handers import client, extra ,callback_quiz, callback_problem, callback_home_work, callback_quizCars, callback_harry_potter, fsmadmin, fsmUser, notification, inline
from database import bot_db, user_db
import asyncio
from handers.notification import scheduler


async def on_startup(_):
    bot_db.sql_create()
    user_db.sql_create_user()
    asyncio.create_task(scheduler())
    print("bot is online")

client.register_handlers_client(dp)

notification.register_handler_notification(dp)
fsmadmin.register_handler_fsmadmin(dp)
fsmUser.register_handler_fsmuser(dp)

callback_quiz.register_handler_callback_quiz(dp)
callback_problem.register_handlers_callback_problem(dp)
callback_home_work.register_handlers_callback_homeWork(dp)
callback_quizCars.register_handlers_callback_homeWork(dp)
callback_harry_potter.register_handlers_callback_homeWork(dp)
inline.register_handler_inline(dp)
extra.register_handlers_extra(dp)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)