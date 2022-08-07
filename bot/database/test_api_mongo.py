from database.api_mongo import save_user_m, get_user_m, init_m, \
save_transaction_m, get_last_transaction_m, confirm_transaction_m, \
get_all_transaction_m
import pytest
import time

cnf = {"database_name": "ss-shop-test", "database_port": "27017", "database_server": "localhost"}

def test_save_user_and_get_user():
    init_m(cnf)
    username = "radmir"
    tg_id = "123467"
    save_user_m(username, tg_id)
    (username, tg_id) = get_user_m(tg_id)
    assert(username == username)

def test_get_user():
    init_m(cnf)
    tg_id = "mnrfbr"
    (username, tg_id) = get_user_m(tg_id=tg_id)
    assert(username == None)


def test_get_last_label_by_id_m():
    init_m(cnf)
    lable = "hello wordl"
    tg_id = "56786787"
    time_created = int(round(time.time() * 100000000))
    amount = 756
    save_transaction_m(lable, tg_id, time_created, amount)
    (tg_id_new, lable_new, time_created_new, amount_new, confirmed_new) = get_last_transaction_m(tg_id)
    assert(lable == lable_new)
    assert(tg_id == tg_id_new)
    assert(amount == amount_new)
    print(confirmed_new)
    print(time_created_new)
    
    time_created = int(round(time.time() * 100000000))
    ok = save_transaction_m(lable, tg_id, time_created, amount)
    assert(ok == False)

def test_confirm_transaction_m():
    init_m(cnf)
    lable = "hello wordl"
    tg_id = "56786787"
    time_created = int(round(time.time() * 100000000))
    amount = 756
    save_transaction_m(lable, tg_id, time_created, amount)
    ok = confirm_transaction_m(lable)  
    assert(ok == True)

def test_get_all_transaction_m():
    init_m(cnf)
    lable = "ffmpg1"
    tg_id = "tochno ya"
    time_created = int(round(time.time() * 100000000))
    amount = 756
    save_transaction_m(lable, tg_id, time_created, amount)
    lable = "ffmpg2"
    tg_id = "tochno ya"
    time_created = int(round(time.time() * 100000000))
    amount = 5045
    save_transaction_m(lable, tg_id, time_created, amount)
    lable = "ffmpg3"
    tg_id = "tochno ya"
    time_created = int(round(time.time() * 1000000000))
    amount = 224
    save_transaction_m(lable, tg_id, time_created, amount)
    confirm_transaction_m(lable)
    
    result = get_all_transaction_m(tg_id)
    count = 0
    for _ in result:
        count += 1
    assert(count == 3)
      



