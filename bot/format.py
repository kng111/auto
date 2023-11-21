import logging
from aiogram import Bot, Dispatcher, types
import asyncio

logging.basicConfig(level=logging.INFO)

API_TOKEN = '6769072442:AAHPHW1_iqZ1D7V4hXiy0i81KW5hu1II5So'  # Замените на свой токен


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который может проверить форматирование сообщения.\nНапишите /check для этого.")

@dp.message_handler(commands=['check'])
async def process_check_command(message: types.Message):
    text = "Пример форматирования:\n<b>жирный</b>, <i>курсив</i>, <code>моноширинный</code>, <a href='http://www.example.com'>ссылка</a>"
    await message.reply(text, parse_mode=types.ParseMode.HTML)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.skip_updates())
