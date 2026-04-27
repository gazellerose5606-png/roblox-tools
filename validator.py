import re

def validate_username(username):
    if not isinstance(username, str):
        raise ValueError('Username must be a string')
    if not 3 <= len(username) <= 20:
        raise ValueError('Username must be between 3 and 20 characters')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValueError('Username can only contain alphanumeric characters and underscores')
    return True


def validate_age(age):
    if not isinstance(age, int):
        raise ValueError('Age must be an integer')
    if not 13 <= age <= 100:
        raise ValueError('Age must be between 13 and 100')
    return True


def validate_email(email):
    if not isinstance(email, str):
        raise ValueError('Email must be a string')
    if not re.match('^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError('Email is not valid')
    return True

