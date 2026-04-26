import os
import json
from typing import Any, Dict, List

def save_to_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def load_from_json(file_path: str) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        return json.load(f)


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]


def get_file_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[1]


def read_file_lines(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        return f.readlines()