from time import sleep
import logging
from functools import wraps

logging.basicConfig(
    filename="timestamp.log",
    format="%(levelname)s %(name)s %(message)s %(asctime)s",
    level=logging.DEBUG,
)

def logtimestamp(original_function):

    @wraps(original_function)
    def WRAPPER(*args, **kwargs):
        logging.debug("Calling %s", original_function.__name__)
        result = original_function(*args, **kwargs)
        return result
    
    return WRAPPER


@logtimestamp
def spam():
    print("SPAM")
    sleep(.5)

@logtimestamp
def ham():
    print("HAM")
    sleep(.5)

for _ in range(5):
    spam()

for _ in range(3):
    ham()

print(ham.__name__, spam.__name__)