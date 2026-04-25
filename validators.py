import json
import re

def is_valid_username(username: str) -> bool:
    return bool(re.match(r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$', username))


def is_valid_user_id(user_id: int) -> bool:
    return isinstance(user_id, int) and user_id > 0


def is_valid_place_id(place_id: int) -> bool:
    return isinstance(place_id, int) and place_id > 0


def is_valid_asset_id(asset_id: int) -> bool:
    return isinstance(asset_id, int) and asset_id > 0


def validate_robot_data(data: str) -> dict:
    try:
        decoded_data = json.loads(data)
        if 'username' in decoded_data and not is_valid_username(decoded_data['username']):
            raise ValueError('Invalid username')
        if 'user_id' in decoded_data and not is_valid_user_id(decoded_data['user_id']):
            raise ValueError('Invalid user ID')
        if 'place_id' in decoded_data and not is_valid_place_id(decoded_data['place_id']):
            raise ValueError('Invalid place ID')
        return decoded_data
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError(f'Invalid data: {e}')