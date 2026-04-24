import logging
from constants import DEFAULT_TIMEOUT
from exceptions import TimeoutError

class RequestHandler:
    def __init__(self, resource_url):
        self.resource_url = resource_url
        self.timeout = DEFAULT_TIMEOUT
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def fetch_data(self):
        try:
            response = self._simulate_request()
            return response
        except TimeoutError:
            self.logger.error('Request timed out')

    def _simulate_request(self):
        import random
        if random.choice([True, False]):
            raise TimeoutError('Simulated timeout')
        return {'data': 'Sample data from ' + self.resource_url}

if __name__ == '__main__':
    handler = RequestHandler('https://api.example.com/data')
    print(handler.fetch_data())