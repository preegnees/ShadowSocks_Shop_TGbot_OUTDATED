from loguru import logger
from .api_mongo import init, hello_mongo, bye_mongo, test_mongo


class IStorage:
    def hello(self):
        pass
    def bye(self):
        pass
    def test(self):
        pass


class Storage(IStorage):
    config = None
    client = None

    def __init__(self, cnf):
        self.config = cnf
        self.clinet = init(self.config)
    def __del__(self):
        self.client.close()
        logger.debug("client mongo closed")
        

    def hello(self) -> str:
        return hello_mongo()
    
    def bye(self) -> str:
        return bye_mongo()
    
    def test(self) -> str:
        return test_mongo(self.config)
