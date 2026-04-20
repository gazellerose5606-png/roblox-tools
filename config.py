import json
import os

DEFAULTS = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'database': 'roblox_db',
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULTS.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key):
        return self.config.get(key, DEFAULTS.get(key))

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)