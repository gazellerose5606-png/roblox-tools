import json
import os

DEFAULT_CONFIG = {
    'setting_1': 'value_1',
    'setting_2': 10,
    'setting_3': True
}

def load_config(filename='config.json'):
    if not os.path.exists(filename):
        return DEFAULT_CONFIG
    with open(filename, 'r') as file:
        config = json.load(file)
    return {**DEFAULT_CONFIG, **config}

if __name__ == '__main__':
    config = load_config()
    print(config)