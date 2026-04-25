import json
import requests

class RobloxAPI:
    BASE_URL = 'https://api.roblox.com/'

    @staticmethod
    def get_user_info(user_id):
        response = requests.get(f'{RobloxAPI.BASE_URL}users/{user_id}')
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_asset_info(asset_id):
        response = requests.get(f'{RobloxAPI.BASE_URL}assets/{asset_id}')
        response.raise_for_status()
        return response.json()

    @staticmethod
    def format_data(data):
        return json.dumps(data, indent=4)

    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'w') as file:
            file.write(RobloxAPI.format_data(data))

user_info = RobloxAPI.get_user_info(1)
RobloxAPI.save_to_file(user_info, 'user_info.json')