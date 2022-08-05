from loguru import logger
from dotenv import dotenv_values
from initialize import run_bot
from database.database.storage import Storage
from middleware.handler import inject_storage

def load_conf() -> dict:
    config = dotenv_values("config.env")
    return config

def main():
    config = load_conf()
    logger.info("envs seccesful loaded")
    storage = Storage(config)
    inject_storage(storage)
    logger.info("database is initialized")
    run_bot(config)

if __name__ == '__main__':
    logger.info("start app")
    main()