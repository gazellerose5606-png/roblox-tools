from typing import List, Dict, Any


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with dict2 values taking precedence."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a nested list into a single list."""
    return [item for sublist in nested_list for item in sublist]


def is_valid_username(username: str) -> bool:
    """Check if a username is valid according to specific rules."""
    return username.isalnum() and 3 <= len(username) <= 20


def calculate_average(numbers: List[float]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)