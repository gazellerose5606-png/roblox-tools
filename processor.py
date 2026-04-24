import json
import logging

logging.basicConfig(level=logging.ERROR)

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        try:
            if not isinstance(self.data, list):
                raise ValueError('Data must be a list')
            return [self._transform(item) for item in self.data]
        except Exception as e:
            logging.error(f'Error processing data: {e}')
            return None

    def _transform(self, item):
        if not isinstance(item, dict):
            raise ValueError('Each item must be a dictionary')
        return {k: v for k, v in item.items() if v is not None}

if __name__ == '__main__':
    processor = DataProcessor([{'a': 1, 'b': None}, {'a': None, 'b': 2}])
    print(json.dumps(processor.process()))
