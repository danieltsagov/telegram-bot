from aiogram import Bot, Dispatcher, types
import logging
from aiogram.utils import executor
import os

# Токен твоего бота, обязательно замени на свой!
API_TOKEN = '8028351293:AAExB4dg56uc8HsFKCyOs27ZGgK8EzEulrc'

# Твой Telegram ID
CHAT_ID = '865376162'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне отзыв и я передам его админам!")

# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Как я могу помочь? Просто отправь команду!")

# Пример отправки сообщения на твой chat_id
async def send_message_to_admin():
    await bot.send_message(CHAT_ID, "Бот запущен и работает!")

# Основной цикл запуска бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)