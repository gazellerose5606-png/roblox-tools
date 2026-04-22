import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_data(file_path, update):
    data = load_data(file_path)
    data.update(update)
    save_data(file_path, data)


def filter_data(data, condition):
    return [item for item in data if condition(item)]


def get_value(data, key, default=None):
    return data.get(key, default)