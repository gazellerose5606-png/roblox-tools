from typing import Dict, Any

# Constants related to Roblox API endpoints.
BASE_URL: str = 'https://api.roblox.com'

ENDPOINTS: Dict[str, str] = {
    'GET_USER': f'{BASE_URL}/users/',
    'GET_GAME': f'{BASE_URL}/games/',
    'GET_ASSET': f'{BASE_URL}/assets/',
}

# Default values for configurations.
DEFAULT_PAGE_SIZE: int = 20
DEFAULT_TIMEOUT: int = 5

def get_endpoint(name: str) -> str:
    """Retrieve the URL for a specific API endpoint.

    Args:
        name (str): The name of the endpoint.

    Returns:
        str: The URL of the specified endpoint, raises KeyError if not found.
    """
    if name not in ENDPOINTS:
        raise KeyError(f'Endpoint {name} not found.')
    return ENDPOINTS[name]

def get_default_page_size() -> int:
    """Get the default page size for pagination.

    Returns:
        int: The default page size.
    """
    return DEFAULT_PAGE_SIZE

def get_default_timeout() -> int:
    """Get the default timeout duration in seconds.

    Returns:
        int: The default timeout duration.
    """
    return DEFAULT_TIMEOUT
