import re

def validate_username(username):
    if not isinstance(username, str) or not username:
        raise ValueError('Username must be a non-empty string')
    if len(username) < 3 or len(username) > 20:
        raise ValueError('Username must be between 3 and 20 characters')
    if not re.match('^[A-Za-z0-9_]+$', username):
        raise ValueError('Username must only contain alphanumeric characters and underscores')


def validate_password(password):
    if not isinstance(password, str) or len(password) < 8:
        raise ValueError('Password must be at least 8 characters long')
    if not re.search('[A-Z]', password) or not re.search('[a-z]', password):
        raise ValueError('Password must contain both uppercase and lowercase letters')
    if not re.search('[0-9]', password):
        raise ValueError('Password must contain at least one digit')


def validate_email(email):
    if not isinstance(email, str) or not email:
        raise ValueError('Email must be a non-empty string')
    if not re.match('[^@]+@[^@]+\.[^@]+', email):
        raise ValueError('Email is not valid')
