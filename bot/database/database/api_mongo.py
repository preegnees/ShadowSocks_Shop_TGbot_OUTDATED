from loguru import logger
from pymongo import MongoClient
from .client_mongo import get_dbclient

client = MongoClient()
cnf = dict()


def init(config: dict):
    global client
    global cnf
    cnf = config
    client = get_dbclient(config)


def save_label(label: str, id_tg: str) -> str:
    return f"ну привет хуле. Вот твой лейбл времменный: {label}, и твой id: {id_tg}"


def save_user(username: str, tg_id: str):
    if username == "" or username == None or tg_id == "" or tg_id == None:
        return False, "username or id_tg is empty"
    filter = {
        "tg_id": tg_id
    }
    update = {
        "$set": {
            "username": username,
            "tg_id": tg_id
        }
    }
    result = client[cnf["database_name"]]["users"].update_one(filter=filter, update=update, upsert=True)
    logger.debug(
        f"save_user. username: {username}, tg_id: {tg_id}, result: {result}")


def get_user(tg_id: str):
    if tg_id == "" or tg_id == None:
        return False, "tg_id is empty"
    request = {
        "tg_id": tg_id
    }
    result = client[cnf["database_name"]]["users"].find_one(request)
    logger.debug(f"get_user. tg_id: {tg_id}, result: {result}")
    if result is None:
        return [None, None]
    return [result["username"], result["tg_id"]]
