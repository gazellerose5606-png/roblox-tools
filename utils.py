import json
import requests

def get_roblox_data(asset_id):
    url = f'https://api.roblox.com/asset/?id={asset_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise ValueError('Failed to fetch data')


def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def load_from_json(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)