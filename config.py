import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.config = default_config if default_config else {}

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                self.config.update(json.load(file))
        else:
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.config, file, indent=4)