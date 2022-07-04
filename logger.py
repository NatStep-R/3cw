import logging


def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("INFO")

    file_log = logging.FileHandler("logs.log",encoding='utf-8')
    logger.addHandler(file_log)

    loger_formate = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_log.setFormatter(loger_formate)

    return logger



