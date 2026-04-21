import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_from_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                file_config = json.load(f)
                self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

if __name__ == '__main__':
    default_config = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    config_loader = ConfigLoader(default_config)
    config_loader.load_from_file('config.json')
    print(config_loader.config)