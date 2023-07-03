from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


button = KeyboardButton("Adminga ma'lumot jo'natish")
keyboard = ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True).row(button)