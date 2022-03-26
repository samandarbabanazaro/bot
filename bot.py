import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5237493961:AAGu0zTYjonwxNRRKZy6qhvas10xv7AIrH0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom Botning Yaratuvchisi Samandar")


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

