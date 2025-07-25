import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

guides = {
    "🎬 Монетизация TikTok (890₽)": "https://your-link.com/tiktok",
    "🌏 Регистрация Alipay без бана (499₽)": "https://your-link.com/alipay",
    "💳 Отмена процентов по кредитке (Тинькофф) (2000₽)": "https://your-link.com/tinkoff"
}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for title in guides:
        kb.add(KeyboardButton(title))
    await message.answer("Привет 👋\n\nВыбери интересующий тебя гайд:", reply_markup=kb)

@dp.message_handler(lambda message: message.text in guides)
async def handle_guide(message: types.Message):
    link = guides[message.text]
    await message.answer(f"Вот твой гайд 📘:\n{link}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
