from typing import List, Dict, Any


def merge_dicts(dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merges a list of dictionaries into a single dictionary.

    Args:
        dicts: A list of dictionaries to merge.

    Returns:
        A single dictionary containing all key-value pairs from the input dictionaries.
    """
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a nested list into a single list.

    Args:
        nested_list: A list of lists to flatten.

    Returns:
        A single list containing all the elements from the nested lists.
    """
    return [item for sublist in nested_list for item in sublist]


def is_integer(value: Any) -> bool:
    """
    Checks if a value is an integer.

    Args:
        value: The value to check.

    Returns:
        True if the value is an integer, False otherwise.
    """
    return isinstance(value, int) 
