from database.api_mongo import save_user, get_user, init
import pytest

cnf = {"database_name": "ss-shop-test", "database_port": "27017", "database_server": "localhost"}

def test_save_user_and_get_user():
    init(cnf)
    username = "radmir"
    tg_id = "123467"
    save_user(username, tg_id)
    (username, tg_id) = get_user(tg_id)
    assert(username == username)

def test_get_user():
    init(cnf)
    tg_id = "mnrfbr"
    (username, tg_id) = get_user(tg_id=tg_id)
    assert(username == None)