import json
import os

def load_config(filename='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            config = json.load(f)
        config = {**defaults, **config}
    else:
        config = defaults
    return config

if __name__ == '__main__':
    default_config = {'key1': 'value1', 'key2': 'value2'}
    config = load_config(defaults=default_config)
    print(config)