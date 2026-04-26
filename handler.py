import json
import requests

class RobloxDataHandler:
    BASE_URL = 'https://api.roblox.com/'

    @staticmethod
    def fetch_data(endpoint):
        response = requests.get(RobloxDataHandler.BASE_URL + endpoint)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_user_info(user_id):
        endpoint = f'users/{user_id}'
        return RobloxDataHandler.fetch_data(endpoint)

    @staticmethod
    def get_game_info(game_id):
        endpoint = f'games/{game_id}'
        return RobloxDataHandler.fetch_data(endpoint)

    @staticmethod
    def get_asset_info(asset_id):
        endpoint = f'assets/{asset_id}'
        return RobloxDataHandler.fetch_data(endpoint)

if __name__ == '__main__':
    user_info = RobloxDataHandler.get_user_info(123456)
    print(json.dumps(user_info, indent=2))