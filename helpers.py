import requests

class RobloxUser:
    def __init__(self, user_id):
        self.user_id = user_id
        self.api_url = f'https://users.roblox.com/v1/users/{self.user_id}'

    def get_user_info(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        return None

def format_user_info(user_info):
    if user_info:
        return f'Username: {user_info.get("name", "Unknown")}\nID: {user_info.get("id", "Unknown")}\nStatus: {user_info.get("description", "No status")}'
    return 'User not found.'

def is_valid_user_id(user_id):
    return isinstance(user_id, int) and user_id > 0
