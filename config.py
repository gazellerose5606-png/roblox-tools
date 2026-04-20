import json
import os

class ConfigLoader:
    def __init__(self, filename, defaults=None):
        self.filename = filename
        self.defaults = defaults or {}
        self.config = self.defaults.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.config.update(json.load(file))

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage:
# loader = ConfigLoader('config.json', {'setting1': 'default_value'})
# print(loader.get('setting1'))