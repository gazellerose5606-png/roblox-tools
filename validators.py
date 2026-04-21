import re

class InputValidator:
    @staticmethod
    def validate_username(username):
        if not isinstance(username, str) or not username:
            raise ValueError('Username must be a non-empty string.')
        if len(username) < 3 or len(username) > 20:
            raise ValueError('Username must be between 3 and 20 characters.')
        if not re.match('^[a-zA-Z0-9_]+$', username):
            raise ValueError('Username can only contain alphanumeric characters and underscores.')

    @staticmethod
    def validate_password(password):
        if not isinstance(password, str) or not password:
            raise ValueError('Password must be a non-empty string.')
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        if not re.search('[A-Z]', password):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not re.search('[a-z]', password):
            raise ValueError('Password must contain at least one lowercase letter.')
        if not re.search('[0-9]', password):
            raise ValueError('Password must contain at least one number.')
        if not re.search('[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError('Password must contain at least one special character.')

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str) or not email:
            raise ValueError('Email must be a non-empty string.')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError('Invalid email format.')