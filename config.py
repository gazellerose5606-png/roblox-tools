import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # use defaults if file not present or invalid

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

# Example default configuration
DEFAULT_CONFIG = {
    'setting1': 'value1',
    'setting2': 10,
    'setting3': True
}

# Usage example
# loader = ConfigLoader(DEFAULT_CONFIG)
# loader.load('user_config.json')
# print(loader.get('setting1'))
