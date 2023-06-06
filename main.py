from aiogram import Bot, Dispatcher, executor, types
from KEY import API
from deep_translator import GoogleTranslator
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(API)
dp = Dispatcher(bot)

lang_from = "ru"
lang_to = "en"


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.username}. Добро пожаловать!\n"
                         f"Напишите /setlang чтобы выбрать язык для перевода.")


@dp.message_handler(commands=['setlang'])
async def set_lang(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=3)
    kb1 = InlineKeyboardButton("Русский/Английский", callback_data="ru/en")
    kb2 = InlineKeyboardButton("Русский/Узбекский", callback_data="ru/uz")
    kb3 = InlineKeyboardButton("Русский/Китайский", callback_data="ru/zh-CN")
    kb4 = InlineKeyboardButton("Английский/Узбекский", callback_data="en/uz")
    kb5 = InlineKeyboardButton("Узбекский/Английский", callback_data="uz/en")
    kb6 = InlineKeyboardButton("Английский/Русский", callback_data="en/ru")

    keyboard.add(kb1, kb2).add(kb3).add(kb4, kb5).add(kb6)
    await message.answer("Выберите язык", reply_markup=keyboard)


@dp.callback_query_handler()
async def translator(callback: types.CallbackQuery):
    global lang_to
    global lang_from
    if callback.data == "ru/en":
        lang_to = callback.data[:2]
        lang_from = callback.data[3:]
        await callback.answer("Вы успешно сменили язык, теперь введите свой текст!", show_alert=True)
    elif callback.data == "ru/uz":
        lang_to = callback.data[:2]
        lang_from = callback.data[3:]
        await callback.answer("Вы успешно сменили язык, теперь введите свой текст!", show_alert=True)
    elif callback.data == "ru/zh-CN":
        lang_to = callback.data[:2]
        lang_from = callback.data[3:]
        await callback.answer("Вы успешно сменили язык, теперь введите свой текст!", show_alert=True)
    elif callback.data == "en/uz":
        lang_to = callback.data[:2]
        lang_from = callback.data[3:]
        await callback.answer("You have successfully changed the language, now enter your text!", show_alert=True)
    elif callback.data == "uz/en":
        lang_to = callback.data[:2]
        lang_from = callback.data[3:]
        await callback.answer("Siz tilni muvaffaqiyatli o'zgartirdingiz, endi matningizni kiriting!", show_alert=True)
    elif callback.data == "en/ru":
        lang_to = callback.data[:2]
        lang_from = callback.data[3:]
        await callback.answer("You have successfully changed the language, now enter your text!", show_alert=True)


@dp.message_handler(content_types=['text'])
async def only_text(message: types.Message):
    text = message.text
    translated = GoogleTranslator(source=lang_to, target=lang_from)
    translated_text = translated.translate(text)
    await message.reply(
        text=f"<b>Перевод:</b> <i>{translated_text}</i> \n "
             f"\n"
             f"<b>Оригинал:</b> <u>{text}</u>",
        parse_mode="HTML"
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
