import logging

logging.basicConfig(
    format='%(levelname)s\t%(name)s\t%(asctime)s\t%(filename)s\t%(lineno)d\t%(message)s', # set the format for log entries
    datefmt="%x-%X",
    filename='../LOGS/formatted.log',
    level=logging.INFO,
)

logging.info("this is information")
logging.warning("this is a warning")
logging.error("this is an ERROR")
value = 38.7
logging.error("Invalid value %s", value)
logging.info("this is information")
logging.critical("this is critical")





