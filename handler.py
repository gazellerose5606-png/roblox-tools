import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def extract_value(data, key):
    return data.get(key)


def update_value(data, key, value):
    data[key] = value


def delete_key(data, key):
    data.pop(key, None)


def merge_data(data1, data2):
    return {**data1, **data2}


def find_item_by_key(data_list, key, value):
    return next((item for item in data_list if item.get(key) == value), None)