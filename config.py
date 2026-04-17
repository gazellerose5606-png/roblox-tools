import os

class Config:
    """Application configuration settings."""

    DEBUG: bool = os.getenv('DEBUG', 'False').lower() in ('true', '1')
    DATABASE_URI: str = os.getenv('DATABASE_URI', 'sqlite:///:memory:')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'your_secret_key')

    @staticmethod
    def get_database_uri() -> str:
        """Return the database URI."""
        return Config.DATABASE_URI

    @staticmethod
    def is_debug() -> bool:
        """Check if debug mode is enabled."""
        return Config.DEBUG

    @staticmethod
    def get_secret_key() -> str:
        """Return the secret key."""
        return Config.SECRET_KEY
