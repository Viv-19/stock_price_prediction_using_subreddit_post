import sys
import logging
from src.logger import logging  # Import the logging you configured

def error_message_detail(error, error_detail: sys):
    """
    Creates a detailed error message with file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file [{file_name}] at line [{line_number}]: {str(error)}"
    return error_message

class StockException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom Exception class for handling application errors.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
