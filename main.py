from aiogram import Bot, Dispatcher, executor, types
from KEY import API
from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardMarkup,
                           KeyboardButton)

bot = Bot(API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.username}. Добро пожаловать!\n"
                         f"Напишите /setlang чтобы выбрать язык для перевода.")


@dp.message_handler(commands=['setlang'])
async def set_lang(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=3)
    kb1 = InlineKeyboardButton("Русский/Английский", callback_data="ru/en")
    kb2 = InlineKeyboardButton("Русский/Узбекский", callback_data="ru/uz")
    kb3 = InlineKeyboardButton("Русский/Китайский", callback_data="ru/cn")
    kb4 = InlineKeyboardButton("Английский/Узбекский", callback_data="en/uz")
    kb5 = InlineKeyboardButton("Узбекский/Английский", callback_data="uz/en")
    kb6 = InlineKeyboardButton("Английский/Русский", callback_data="en/ru")

    keyboard.add(kb1, kb2).add(kb3).add(kb4, kb5).add(kb6)
    await message.answer("Выберите язык", reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp)
