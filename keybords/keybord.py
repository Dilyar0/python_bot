from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_quiz = KeyboardButton("/quiz")
button_problem = KeyboardButton("/problem")
button_garry_potter = KeyboardButton("/garry_potter")
button_car_quiz = KeyboardButton("/car_quiz")

keyboardStat = ReplyKeyboardMarkup(resize_keyboard=True)
keyboardStat.row(button_quiz, button_problem, button_garry_potter, button_car_quiz)