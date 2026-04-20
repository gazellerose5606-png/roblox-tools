import json

DEFAULT_CONFIG = {
    'username': 'guest',
    'max_players': 50,
    'game_mode': 'survival',
    'show_notifications': True
}

def load_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
            return {**DEFAULT_CONFIG, **config}
    except FileNotFoundError:
        return DEFAULT_CONFIG
    except json.JSONDecodeError:
        return DEFAULT_CONFIG
