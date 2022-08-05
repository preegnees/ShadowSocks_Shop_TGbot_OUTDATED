from loguru import logger
from dotenv import dotenv_values
from ui.initialize import run_bot
from database.storage import Storage
from ui.handler import set_storage_to_handlers

def load_conf() -> dict:
    config = dotenv_values("config.env")
    return config

def main():
    config = load_conf()
    logger.info("envs seccesful loaded")
    storage = Storage(config)
    set_storage_to_handlers(storage)
    logger.info("database is initialized")
    run_bot(config)

if __name__ == '__main__':
    logger.info("start app")
    main()