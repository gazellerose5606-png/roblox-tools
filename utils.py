import json
import requests

def fetch_roblox_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def get_roblox_user_data(user_id):
    url = f'https://users.roblox.com/v1/users/{user_id}'
    return fetch_roblox_data(url)


def get_roblox_game_data(game_id):
    url = f'https://games.roblox.com/v1/games/{game_id}'
    return fetch_roblox_data(url)