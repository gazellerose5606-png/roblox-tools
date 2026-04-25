import json

def load_roblox_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_roblox_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_value(data, key, default=None):
    return data.get(key, default)


def set_value(data, key, value):
    data[key] = value


def delete_key(data, key):
    if key in data:
        del data[key]