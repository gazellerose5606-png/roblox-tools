import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        config_path = os.getenv('CONFIG_PATH', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                user_config = json.load(file)
            return {**self.default_config, **user_config}
        return self.default_config

    def get(self, key):
        return self.config.get(key)

# Example usage
if __name__ == '__main__':
    defaults = {'setting1': 'default_value1', 'setting2': 'default_value2'}
    config_loader = ConfigLoader(defaults)
    print(config_loader.get('setting1'))
    print(config_loader.get('setting2'))
