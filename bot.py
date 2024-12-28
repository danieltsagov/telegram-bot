from flask import Flask
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

API_TOKEN = "8028351293:AAExB4dg56uc8HsFKCyOs27ZGgK8EzEulrc"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(commands=['start'])
async def send_welcome(message: Message):
    await message.answer("Привет! Я перешлю ваши сообщения админам.")

# Flask сервер для поддержки Web Service
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем aiogram в asyncio
    asyncio.get_event_loop().create_task(run_bot())
    # Запуск Flask для работы Web Service
    app.run(host='0.0.0.0', port=8080)