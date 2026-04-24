from typing import Final

BASE_URL: Final[str] = "https://www.roblox.com"
API_VERSION: Final[int] = 1
DEFAULT_TIMEOUT: Final[int] = 30

class GameStatus:
    ACTIVE: Final[str] = "active"
    INACTIVE: Final[str] = "inactive"
    MAINTENANCE: Final[str] = "maintenance"

class UserRoles:
    ADMIN: Final[str] = "admin"
    MODERATOR: Final[str] = "moderator"
    PLAYER: Final[str] = "player"

class ErrorMessages:
    USER_NOT_FOUND: Final[str] = "User not found"
    GAME_NOT_FOUND: Final[str] = "Game not found"
    INVALID_REQUEST: Final[str] = "Invalid request"

class Config:
    RETRY_ATTEMPTS: Final[int] = 3
    MAX_CONNECTIONS: Final[int] = 10
    REQUEST_TIMEOUT: Final[int] = 15