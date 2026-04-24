import json
import requests

class RobloxAPI:
    BASE_URL = 'https://api.roblox.com/'

    @staticmethod
    def fetch_data(endpoint):
        response = requests.get(f'{RobloxAPI.BASE_URL}{endpoint}')
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_user_info(user_id):
        endpoint = f'users/{user_id}'
        return RobloxAPI.fetch_data(endpoint)

    @staticmethod
    def get_game_info(game_id):
        endpoint = f'games/{game_id}'
        return RobloxAPI.fetch_data(endpoint)

    @staticmethod
    def get_asset_info(asset_id):
        endpoint = f'assets/{asset_id}'
        return RobloxAPI.fetch_data(endpoint)

    @staticmethod
    def save_to_json(data, file_name):
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def load_from_json(file_name):
        with open(file_name, 'r') as json_file:
            return json.load(json_file)