def load_data(file_path):
    import json
    with open(file_path, 'r') as f:
        return json.load(f)


def save_data(file_path, data):
    import json
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def get_player_statistics(player_id, data):
    return data.get('players', {}).get(player_id, {})


def update_player_statistics(player_id, stats, data):
    data['players'][player_id] = stats


def filter_items_by_type(data, item_type):
    return [item for item in data.get('items', []) if item['type'] == item_type]
