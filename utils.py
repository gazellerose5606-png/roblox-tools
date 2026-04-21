import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def validate_data(schema, data):
    from jsonschema import validate, ValidationError
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return e.message
    return None


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]