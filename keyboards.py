from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard = InlineKeyboardMarkup(row_width=3)
kb1 = InlineKeyboardButton("Русский/Английский", callback_data="ru/en")
kb2 = InlineKeyboardButton("Русский/Узбекский", callback_data="ru/uz")
kb3 = InlineKeyboardButton("Русский/Китайский", callback_data="ru/zh-CN")
kb4 = InlineKeyboardButton("Английский/Узбекский", callback_data="en/uz")
kb5 = InlineKeyboardButton("Узбекский/Английский", callback_data="uz/en")
kb6 = InlineKeyboardButton("Английский/Русский", callback_data="en/ru")

keyboard.add(kb1, kb2).add(kb3).add(kb4, kb5).add(kb6)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
r1 = KeyboardButton(text="Выбрать-язык")
r2 = KeyboardButton(text="Перевести")
r3 = KeyboardButton(text="Помощь")
r4 = KeyboardButton(text="О боте")
keyboard1.add(r1, r2)
keyboard1.add(r3, r4)

