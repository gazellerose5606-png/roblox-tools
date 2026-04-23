from typing import Any, Dict, Union


def validate_identifier(identifier: str) -> bool:
    """Validate Roblox identifier.

    An identifier must start with a letter and can
    only contain alphanumeric characters and underscores.

    Args:
        identifier (str): The identifier to validate.

    Returns:
        bool: True if valid, otherwise False.
    """
    return identifier.isidentifier()


def validate_player_data(data: Dict[str, Any]) -> bool:
    """Validate player data structure.

    Checks if the data contains required keys and
    type constraints: 'name' (str), 'age' (int).

    Args:
        data (Dict[str, Any]): The player data to validate.

    Returns:
        bool: True if data is valid, otherwise False.
    """
    required_keys = {'name': str, 'age': int}
    return all(
        key in data and isinstance(data[key], required_keys[key])
        for key in required_keys
    )


def is_valid_color(value: Union[str, int]) -> bool:
    """Check if the color value is valid.

    A valid color can be an integer between 0 and 16777215
    or a hex color string starting with '#' followed by 6 hex digits.

    Args:
        value (Union[str, int]): The color value to check.

    Returns:
        bool: True if valid, otherwise False.
    """
    if isinstance(value, int):
        return 0 <= value <= 16777215
    if isinstance(value, str) and value.startswith('#'):
        return len(value) == 7 and all(c in '0123456789abcdef' for c in value[1:])
    return False