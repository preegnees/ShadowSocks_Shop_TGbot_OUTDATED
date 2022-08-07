from loguru import logger

storage = None

def inject_storage(strg):
    global storage
    storage = strg
    logger.debug("Произошло инжек хранилища в файл handler")
    

def process_start_command_handler(tg_id: str, fullname: str) -> str:
    storage.save_user(fullname, tg_id)
    (username, id) = storage.get_user(tg_id)
    return f"username: {username}, id: {id}"
    