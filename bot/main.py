from loguru import logger
from dotenv import dotenv_values

def load_conf() -> dict:
    config = dotenv_values("config.env")
    return config

def main():
    load_conf()
    logger.info("envs seccesful loaded")

if __name__ == '__main__':
    logger.info("start app")
    main()