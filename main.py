from aiogram import Bot, Dispatcher, executor, types
from KEY import API
from deep_translator import GoogleTranslator
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text

bot = Bot(API)
dp = Dispatcher(bot)

lang_from = "ru"
lang_to = "en"

HELP = """
<b>Не получается запустить бота?</b>
<i>Для начало нужно запустить бота</i> - /start
<i>Выбрать язык</i> - /setlang
<i>Ввести текст и подождать...</i>

Если возникли трудности или нашли баг(ошибку), то вы можете связяться с админом бота @xmn2003.
"""

keyboard = InlineKeyboardMarkup(row_width=3)
kb1 = InlineKeyboardButton("Русский/Английский", callback_data="ru/en")
kb2 = InlineKeyboardButton("Русский/Узбекский", callback_data="ru/uz")
kb3 = InlineKeyboardButton("Русский/Китайский", callback_data="ru/zh-CN")
kb4 = InlineKeyboardButton("Английский/Узбекский", callback_data="en/uz")
kb5 = InlineKeyboardButton("Узбекский/Английский", callback_data="uz/en")
kb6 = InlineKeyboardButton("Английский/Русский", callback_data="en/ru")

keyboard.add(kb1, kb2).add(kb3).add(kb4, kb5).add(kb6)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    r1 = KeyboardButton(text="Выбрать-язык")
    r2 = KeyboardButton(text="Перевести")
    r3 = KeyboardButton(text="Помощь")
    r4 = KeyboardButton(text="О боте")
    keyboard1.add(r1, r2)
    keyboard1.add(r3, r4)
    await message.answer(f"Привет, {message.from_user.username}. Добро пожаловать!\n"
                         f"Напишите /setlang чтобы выбрать язык для перевода.", reply_markup=keyboard1)


@dp.message_handler(Text(equals=['Помощь']))
async def help(message: types.Message):
    await message.answer(HELP, parse_mode="HTML")


@dp.message_handler(Text(equals=['Выбрать-язык']))
async def choice_lang(message: types.Message):
    await message.answer(text="Выберите язык", reply_markup=keyboard)


@dp.message_handler(Text(equals=['Перевести']))
async def translate_texts(message: types.Message):
    await message.answer(text=f"<b>Язык ввода: {lang_to}\n"
                              f"Язык перевода: {lang_from}\n</b>"
                              f"Хотите изменить? <i>/setlang</i>\n"
                              f"Введите свой текст 👇", parse_mode="HTML")


@dp.message_handler(Text(equals=['О боте']))
async def choice_lang(message: types.Message):
    await message.answer(text="<b>Бот Переводчик</b>\n"
                              "Поддерживает 4 языка для перевода\n"
                              "Создан при помощи Python(Aiogram),а также используется библиотека deep-translator 1.11.1\n"
                              "Связаться со админом - <b>@xmn2003</b>\n", parse_mode="HTML")


@dp.message_handler(commands=['setlang'])
async def set_lang(message: types.Message):
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
        await callback.answer("Siz tilni muvaffaqiyatli o'zgartirdingiz, endi matningizni kiriting!",
                              show_alert=True)
    elif callback.data == "en/ru":
        lang_to = callback.data[:2]
        lang_from = callback.data[3:]
        await callback.answer("You have successfully changed the language, now enter your text!", show_alert=True)


@dp.message_handler(content_types=['text'])
async def only_text(message: types.Message):
    try:
        text = message.text
        translated = GoogleTranslator(source=lang_to, target=lang_from)
        translated_text = translated.translate(text)
        await message.reply(
            text=f"<b>Перевод:</b> <i>{translated_text}</i> \n "
                 f"\n"
                 f"<b>Оригинал:</b> <u>{text}</u>",
            parse_mode="HTML"
        )

    except:
        await message.reply("Пожалуйста введите, корректный текст!!!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
