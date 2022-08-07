from loguru import logger
import calendar
import datetime

def get_payment_link(storage, id_tg):
    pass
    
def get_status(storage, id) -> str:
    if _verification_user(storage, id) == False:
        logger.error(f"username is None, id: {id}")
        exit(0)
    status = _create_status(storage, id)
    return status
    
def get_history(storage, id):
    pass
    


def _verification_user(storage, id) -> bool:
    username, tg_id = storage.get_user(id)
    if username == None or tg_id == None:
        return False
    return True

def _gen_lable():
    return ["label", 12334566]

def _create_status(storage, id) -> str:
    status = ""
    (_, _, time_created, amount, confirmed) = storage.get_last_transaction(id)
    if _whether_to_send_config(time_created, confirmed) == False:
        status = _bad_status()
    else:
        status = _good_status(time_created, amount)
    return status

def _bad_status() -> str:
    stauts = f"--> Вы не оплатитли этот месяц;"
    return stauts

def _good_status(time_created, amount) -> str:
    # тут где то нужно получить конфигурацию
    conf = "Тут должна быть конфигурация"
    date = _milliseconds_to_human_date(time_created)
    stauts = f"--> оплачено до конца этого месяца;\nдата оплаты: {date};\nсумма: {amount} руб.\nваша конфигурация: {conf}"
    return stauts

def _whether_to_send_config(time_created, confirmed) -> bool:
    tc = _milliseconds_to_human_date(time_created)
    
    tc_year = tc.split("-")[0]
    tc_month = tc.split("-")[1]
    tc_day = tc.split("-")[2]
    
    currentDate = datetime.date.today()
    cd = str(datetime.date(
        currentDate.year, currentDate.month, 
        calendar.monthrange(currentDate.year, currentDate.month
    )[1]))
    
    cd_year = cd.split("-")[0]
    cd_month = cd.split("-")[1]
    cd_day = cd.split("-")[2]
    
    if cd_year == tc_year:
        if cd_month == tc_month:
            if cd_day >= tc_day:
                if confirmed == 1:
                    return True
    return False

def _milliseconds_to_human_date(mill_date) -> str:
    date = str(datetime.datetime.fromtimestamp(
    mill_date / 1000.0, tz=datetime.timezone.utc
    )).split(" ")[0] # 1000 получить из конфига
    return date