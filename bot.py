from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio

API_TOKEN = "8028351293:AAExB4dg56uc8HsFKCyOs27ZGgK8EzEulrc"
ADMIN_ID = 865376162  # Ваш Telegram ID

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message_handler(commands=["start"])  # Новый синтаксис
async def start_handler(message: Message):
    await message.reply("Привет! Я бот, который работает в фоновом режиме и пересылает ваши сообщения админам.")

# Фоновая задача
async def periodic_task():
    while True:
        try:
            await bot.send_message(chat_id=ADMIN_ID, text="Фоновая задача работает!")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        await asyncio.sleep(3600)  # Каждые 60 минут

# Запуск бота
async def main():
    dp.include_router(dp.router)  # Добавление маршрутизатора
    asyncio.create_task(periodic_task())  # Запуск фоновой задачи
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())