from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

from keyboards import main_keyboard
from config_data import API_ID, API_HASH, BOT_TOKEN  # явно импортируем

bot = Client(
    name="BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@bot.on_message(filters.command("start"))
async def command_start(client: Client, message: Message):
    await message.reply("Бот запущен!", reply_markup=main_keyboard)

@bot.on_message(filters.command("help"))
async def command_help(client: Client, message: Message):
    await message.reply("/help")

@bot.on_message(filters.command("datetime"))
async def show_datetime(client: Client, message: Message):  # переименовал
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    await message.reply(f"Дата: {date_str}\nВремя: {time_str}")

@bot.on_message(filters.command("date"))
async def show_date(client: Client, message: Message):
    date_str = datetime.now().strftime("%Y-%m-%d")
    await message.reply(f"Дата сегодняшнего дня: {date_str}")

@bot.on_message(filters.command("time"))
async def show_time(client: Client, message: Message):
    time_str = datetime.now().strftime("%H:%M:%S")
    await message.reply(f"Нынешнее время: {time_str}")

@bot.on_message()
async def echo(client: Client, message: Message):
    await message.reply(f"Я не знаю эту команду: {message.text}. Попробуйте /help")

bot.run()