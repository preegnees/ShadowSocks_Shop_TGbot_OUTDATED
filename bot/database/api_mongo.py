from loguru import logger
from .client_mongo import get_dbclient

client = None
def init(config: dict):
    global client
    client = get_dbclient(config)

def hello_mongo() -> str:
    return "ну привет хуле"

def bye_mongo() -> str:
    return "приходи еще черт"

def test_mongo(config: dict) -> str:
    return config["token"]

