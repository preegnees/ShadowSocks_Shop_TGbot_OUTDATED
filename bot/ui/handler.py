storage = None


def set_storage_to_handlers(strg):
    global storage
    storage = strg


def process_start_command_handler() -> str:
    return storage.hello()


def procss_bye_command_handler(message: str) -> str:
    return message


def procss_test_command_handler() -> str:
    return storage.test()
