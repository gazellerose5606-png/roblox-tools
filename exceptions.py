class RobloxError(Exception):
    """Base class for other exceptions."""
    pass

class InvalidAssetIDError(RobloxError):
    """Raised when an asset ID is invalid."""
    def __init__(self, asset_id):
        self.asset_id = asset_id
        super().__init__(f'Invalid asset ID: {self.asset_id}')

class AssetNotFoundError(RobloxError):
    """Raised when an asset is not found."""
    def __init__(self, asset_id):
        self.asset_id = asset_id
        super().__init__(f'Asset not found: {self.asset_id}')

class RateLimitExceededError(RobloxError):
    """Raised when API rate limits are exceeded."""
    pass

class AuthenticationError(RobloxError):
    """Raised when authentication fails."""
    def __init__(self, message):
        super().__init__(message)

class NetworkError(RobloxError):
    """Raised for network-related issues."""
    def __init__(self, message):
        super().__init__(message)