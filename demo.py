# from src.logger import logging  

# def main():
#     logging.info("This is an INFO message ")
#     logging.debug("This is a DEBUG message ")
#     logging.warning("This is a WARNING message ")
#     logging.error("This is an ERROR message ")
#     logging.critical("This is a CRITICAL message ")

# if __name__ == "__main__":
#     main()



from src.logger import logging
from src.exception import StockException
import sys

def main():
    try:
        a = 1 / 0  # Forcefully creating a ZeroDivisionError
    except Exception as e:
        logging.error("Exception occurred")
        raise StockException(e, sys)

if __name__ == "__main__":
    main()