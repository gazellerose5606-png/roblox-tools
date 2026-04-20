import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        return False
    if not 1 <= len(user_input) <= 100:
        return False
    if not re.match('^[a-zA-Z0-9_ ]*$', user_input):
        return False
    return True

def process_user_input(user_input):
    if not validate_input(user_input):
        raise ValueError('Invalid input')
    # Process the valid input here
    print(f'Processing: {user_input}')