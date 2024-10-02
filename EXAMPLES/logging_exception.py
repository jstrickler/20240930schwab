import logging

logging.basicConfig( # configure logging
    filename='../LOGS/exception.log',
    level=logging.WARNING,  # minimum level
)

for i in range(3):
    try:
        result = i/0
    except ZeroDivisionError:
        # logging.error("message", exc_info=True)
        logging.exception('Logging with exception info') # add exception info to the log
