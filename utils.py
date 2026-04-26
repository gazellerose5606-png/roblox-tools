import requests

BASE_URL = 'https://api.roblox.com/'


def fetch_roblox_data(endpoint):
    response = requests.get(f'{BASE_URL}{endpoint}')
    response.raise_for_status()
    return response.json()


def get_user_info(user_id):
    try:
        return fetch_roblox_data(f'users/{user_id}')
    except requests.RequestException as e:
        return {'error': str(e)}


def get_game_info(game_id):
    try:
        return fetch_roblox_data(f'games/{game_id}')
    except requests.RequestException as e:
        return {'error': str(e)}


def get_asset_info(asset_id):
    try:
        return fetch_roblox_data(f'assets/{asset_id}')
    except requests.RequestException as e:
        return {'error': str(e)}
