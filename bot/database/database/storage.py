from loguru import logger
from .api_mongo import init_m, save_user_m, get_user_m, save_transaction_m, get_all_transaction_m, get_last_transaction_m, confirm_transaction_m

class IStorage:
    def get_user(self, id_tg: str):
        pass
    
    def save_user(self, username: str, id_tg: str):
        pass
    
    
    
    def save_transaction(seld, lable: str, id_tg: str, time_created: int, amount: int, confirmed: bool):
        pass
    
    def get_all_ltransactions(id_tg: str):
        pass
    
    def get_last_transaction(id_tg: str):
        pass
    
    def confirm_transaction(lable: str):
        pass

class Storage(IStorage):
    config = None
    client = None

    def __init__(self, cnf):
        self.config = cnf
        self.clinet = init_m(self.config)
    
    def save_user(self, username: str, id_tg: str):
        save_user_m(username, id_tg)
        
    def get_user(self, id_tg: str):
        (username, tg_id) = get_user_m(id_tg)
        return username, tg_id
    
    
    
    def save_transaction(seld, lable: str, id_tg: str, time_created: int, amount: int):
        save_transaction_m(lable, id_tg, time_created, amount)
    
    def get_all_ltransactions(id_tg: str):
        pass
    
    def get_last_transaction(id_tg: str):
        get_last_transaction_m(id_tg)
    
    def confirm_transaction(lable: str):
        confirm_transaction_m(lable)