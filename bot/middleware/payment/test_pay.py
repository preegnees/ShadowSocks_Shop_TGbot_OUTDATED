from payment.pay import get_status
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

def test_get_status():
    storage = Storage_Mock()
    status = get_status(storage, "test_id_3456")
    storage2 = Storage_Mock2()
    status2 = get_status(storage2, "test_id_3456")
    assert(status != status2)