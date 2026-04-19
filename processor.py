import time
import json

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def optimize_data(self):
        start_time = time.time()
        optimized_data = {k: v for k, v in self.data.items() if v}
        end_time = time.time()
        print(f"Optimization took {end_time - start_time:.4f} seconds")
        return optimized_data

    def process_data(self):
        optimized_data = self.optimize_data()
        # Simulate data processing
        processed_data = json.dumps(optimized_data)
        return processed_data

if __name__ == '__main__':
    raw_data = {'key1': 'value1', 'key2': None, 'key3': 'value3'}
    processor = DataProcessor(raw_data)
    result = processor.process_data()
    print(result)