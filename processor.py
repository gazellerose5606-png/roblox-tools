import json
import logging

class Processor:
    def __init__(self, data):
        self.data = data
        self.results = []
        self.logger = logging.getLogger(__name__)

    def process(self):
        try:
            self.validate_data()
            self.results = [self.process_item(item) for item in self.data]
        except ValueError as ve:
            self.logger.error(f'ValueError occurred: {ve}')
        except TypeError as te:
            self.logger.error(f'TypeError occurred: {te}')
        except Exception as e:
            self.logger.error(f'Unexpected error: {e}')

    def validate_data(self):
        if not isinstance(self.data, list):
            raise TypeError('Data should be a list')
        if not self.data:
            raise ValueError('Data list is empty')

    def process_item(self, item):
        if not isinstance(item, dict):
            raise ValueError('Each item must be a dictionary')
        return {k: v for k, v in item.items() if v is not None}

    def get_results(self):
        return json.dumps(self.results)