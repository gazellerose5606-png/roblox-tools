import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, config_file='config.json', defaults=None):
        self.config_file = Path(config_file)
        self.defaults = defaults or {}
        self.config = self.load_config()

    def load_config(self):
        if self.config_file.is_file():
            with open(self.config_file, 'r') as f:
                return {**self.defaults, **json.load(f)}
        return self.defaults

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self, new_config):
        with open(self.config_file, 'w') as f:
            json.dump({**self.config, **new_config}, f, indent=4)