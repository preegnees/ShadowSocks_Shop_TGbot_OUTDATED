from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from loguru import logger
from aiogram.utils import executor
from middleware.handler import process_start_command_handler


def run_bot(config: dict):    
    cnf = config
    token = cnf["token"]
    if token == None or token == "":
        logger.error("token is empty")
        exit(0)
    try:
        bot = Bot(cnf["token"])
    except:
        logger.error("tokent is invalid")
        exit(0)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def process_start_command(message: types.Message):
        await message.reply(process_start_command_handler(message.from_user.id, message.from_user.username))

    logger.info("bot is initialized")
    executor.start_polling(dp)