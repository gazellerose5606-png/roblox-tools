import os
import json
from typing import Any, Dict

def read_json_file(file_path: str) -> Dict[str, Any]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_files_in_directory(directory: str) -> list:
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a directory")
    return os.listdir(directory)


def ensure_directory_exists(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)


def is_valid_filename(filename: str) -> bool:
    try:
        filename.encode('ascii')  # Validate ASCII
        return True
    except UnicodeEncodeError:
        return False