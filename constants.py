from typing import Final

VERSION: Final[str] = '1.0.0'
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 5
API_URL: Final[str] = 'https://api.roblox.com/'

COLORS: Final[dict] = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
}

PLAYER_STATUSES: Final[list] = [
    'Offline',
    'Online',
    'In-Game',
    'Busy',
]

ROLE_IDS: Final[dict] = {
    'Admin': 1,
    'Mod': 2,
    'User': 3,
}

