import logging
from exceptions import CustomException
from utils import validate_input, process_data

class Handler:
    def __init__(self, data):
        self.data = data

    def handle(self):
        try:
            if validate_input(self.data):
                result = process_data(self.data)
                self.log_result(result)
            else:
                raise CustomException("Invalid input")
        except CustomException as e:
            logging.error(f'Error: {e}')

    def log_result(self, result):
        logging.info(f'Processing result: {result}')