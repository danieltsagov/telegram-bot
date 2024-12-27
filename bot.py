from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import logging

# Токен от BotFather
TOKEN = "8028351293:AAExB4dg56uc8HsFKCyOs27ZGgK8EzEulrc"
# Твой Telegram ID
YOUR_CHAT_ID = 865376162

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

# Обработка команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напиши сообщение и я перешлю его админам.")

# Пересылка любого сообщения
@dp.message()
async def forward_message(message: types.Message):
    print(f"Получено сообщение от {message.from_user.username} с chat_id: {message.chat.id}")
    await bot.forward_message(chat_id=YOUR_CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())