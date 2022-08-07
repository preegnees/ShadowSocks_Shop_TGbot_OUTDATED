from payment.pay import get_status, get_history
import pytest
import time

class Storage_Mock():
    def get_user(self, id: str):
        return ["test_user","test_id_3456"] 
    def get_last_transaction(self, id: str):
        return ["test_id_3456", "label_test", int(time.time() * 1000), 500, 1]

class Storage_Mock2():
    def get_user(self, id: str):
        return ["test_user","test_id_3456"] 
    def get_last_transaction(self, id: str):
        return ["test_id_3456", "label_test", int(time.time() * 1000), 500, 0]
    
class Storage_Mock3():
    def get_user(self, id: str):
        return ["test_user","test_id_3456"] 
    def get_all_transaction(self, id: str):
        return [{"id_tg": "test_id_3456", "lable": "label_test", "time_created": int(time.time() * 1000) + 2, "amount": 356, "confirmed": 0}, 
                {"id_tg": "test_id_3456", "lable": "lolkekcheburel", "time_created": int(time.time() * 1000) + 1, "amount": 778, "confirmed": 1},
                {"id_tg": "test_id_3456", "lable": "pochemutakblyat", "time_created": int(time.time() * 1000) + 0, "amount": 34, "confirmed": 1}]

def test_get_status():
    storage = Storage_Mock()
    status = get_status(storage, "test_id_3456")
    storage2 = Storage_Mock2()
    status2 = get_status(storage2, "test_id_3456")
    assert(status != status2)

def test_get_history():
    storage = Storage_Mock3()
    history = get_history(storage, "test_id_3456")
    assert("-->1" in history and "-->2" in history)