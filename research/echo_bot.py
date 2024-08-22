from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging


load_dotenv()
API_TOKEN =  os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi!\n I am an Echo Bot!\n Powered by Aiogram")


@dp.message_handler()
async def echo(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)