from pymongo import MongoClient
from loguru import logger

def get_dbclient(config: dict) -> MongoClient:
    SERVER = config["database_server"]
    PORT = config["database_port"]
    URL = f"mongodb://{SERVER}:{PORT}"
    logger.debug("URL: ", URL)
    client = MongoClient(URL)
    try:
        client.admin.command("ping")
    except Exception:
        logger.error("err connection to database")
        exit(0)
    logger.info("seccesfull connect to database")
    return client