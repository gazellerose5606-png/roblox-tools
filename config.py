import json
import os

DEFAULT_CONFIG = {
    'api_key': 'your_api_key',
    'timeout': 30,
    'retries': 3,
    'log_level': 'INFO'
}

class ConfigLoader:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.config[key] = value
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)