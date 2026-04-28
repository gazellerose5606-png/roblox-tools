import json
import os

class ConfigLoader:
    def __init__(self, default_config_filepath):
        self.defaults = self.load_json(default_config_filepath)
        self.config = self.defaults.copy()

    def load_json(self, filepath):
        if not os.path.exists(filepath):
            return {}
        with open(filepath, 'r') as file:
            return json.load(file)

    def update(self, custom_config_filepath):
        custom_config = self.load_json(custom_config_filepath)
        self.config.update(custom_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.config, file, indent=4)

    def reset(self):
        self.config = self.defaults.copy()

# Usage Example:
# config_loader = ConfigLoader('default_config.json')
# config_loader.update('custom_config.json')
# value = config_loader.get('key', 'default_value')