from loguru import logger
from .api_mongo import init, save_label, save_user, get_user

class IStorage:
    def set_lable(self, lable: str, id_tg: str):
        pass
    
    def set_user(self, username: str, id_tg: str):
        pass


class Storage(IStorage):
    config = None
    client = None

    def __init__(self, cnf):
        self.config = cnf
        self.clinet = init(self.config)
        

    def set_lable(self, label: str, id_tg: str):
        save_label(label, id_tg)
    
    def set_user(self, username: str, id_tg: str):
        save_user(username, id_tg)
        
    def get_user(self, id_tg: str):
        (username, tg_id) = get_user(id_tg)
        return username, tg_id