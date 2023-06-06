from aiogram import Bot, Dispatcher, executor, types
from KEY import API
from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardMarkup,
                           KeyboardButton)

bot = Bot(API)
dp = Dispatcher(bot)

if __name__ == "__main__":
    executor.start_polling(dp)
