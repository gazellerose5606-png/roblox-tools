def get_user_id(username, user_data):
    for user in user_data:
        if user['username'] == username:
            return user['id']
    return None

def calculate_playtime(start_time, end_time):
    return (end_time - start_time).seconds

def format_user_data(user):
    return {
        'id': user['id'],
        'username': user['username'],
        'status': user['status']
    }

def filter_active_users(user_data):
    return [user for user in user_data if user['status'] == 'active']

import json

def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json_file(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
