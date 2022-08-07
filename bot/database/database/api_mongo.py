from loguru import logger
from pymongo import MongoClient
import pymongo
from .client_mongo import get_dbclient
from bson.son import SON


client = MongoClient()
cnf = dict()


def init_m(config: dict):
    global client
    global cnf
    cnf = config
    client = get_dbclient(config)


def save_user_m(username: str, tg_id: str):
    if username == "" or username == None or tg_id == "" or tg_id == None:
        return False, "username or id_tg is empty"
    filter = {
        "tg_id": tg_id
    }
    update = {
        "$set": {
            "username": "@" + username,
            "tg_id": tg_id
        }
    }
    result = client[cnf["database_name"]]["users"].update_one(
        filter=filter, update=update, upsert=True)
    logger.debug(
        f"save_user. username: {username}, tg_id: {tg_id}, result: {result}")


def get_user_m(tg_id: str):
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

def save_transaction_m(lable: str, id_tg: str, time_created: int, amount: int):    
    get = {
        "lable": lable,
    }
    res = client[cnf["database_name"]]["label_and_id"].find_one(get)
    if res != None:
        logger.error("this label already exists")
        return False
    
    if lable == "" or lable == None or id_tg == "" or \
        id_tg == None or time_created == 0 or time_created == None or amount == 0 or amount == None:
        return False, f"incorrent data. lable = {lable}, id_tg = {id_tg}, time_created = {time_created}, amount = {amount}"
    logger.debug(f"lable = {lable}, id_tg = {id_tg}, time_created = {time_created}")
    
    insert = {
        "id_tg": id_tg,
        "lable": lable,
        "time_created": time_created,
        "amount": amount,
        "confirmed": 0
    }
    result = client[cnf["database_name"]]["label_and_id"].insert_one(insert)
    if result != None:
        return True
    return False, "result is None"

def get_all_transaction_m(id_tg: str):
    if id_tg == "" or id_tg == None:
        return False, "id_tg is empty"
    find = {
        "id_tg": id_tg
    }
    result = client[cnf["database_name"]]["label_and_id"].find(find).sort("time_started", -1)
    logger.debug(f"get_all_transaction_m. tg_id: {id_tg}, result: {result}")
    if result is None:
        return [None, None, None, None, None]
    return result

def get_last_transaction_m(id_tg: str):
    if id_tg == "" or id_tg == None:
        return False, "id_tg is empty"
    find = {
        "id_tg": id_tg
    }
    result = client[cnf["database_name"]]["label_and_id"].find(find).sort("time_created", -1).limit(1)[0]
    logger.debug(f"get_last_transaction_m. tg_id: {id_tg}, result: {result}")
    if result is None:
        return [None, None, None, None, None]
    return [result["id_tg"], result["lable"], result["time_created"], result["amount"], result["confirmed"]]

def confirm_transaction_m(lable: str):
    filter = {
        "lable": lable
    }
    update = {
        "$set": {
            "confirmed": 1
        }
    }
    result = client[cnf["database_name"]]["label_and_id"].update_one(filter, update)
    if result != None:
        return True
    return False