import json
import re

class InputValidationError(Exception):
    pass

def validate_input(data):
    if not isinstance(data, dict):
        raise InputValidationError('Input must be a dictionary.')
    if 'username' not in data or not isinstance(data['username'], str):
        raise InputValidationError('Username is required and must be a string.')
    if 'age' in data:
        if not isinstance(data['age'], int) or data['age'] < 0:
            raise InputValidationError('Age must be a non-negative integer.')
    if 'email' in data:
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', data['email']):
            raise InputValidationError('Invalid email format.')

def process_data(data):
    try:
        validate_input(data)
        # Process the valid input data
        return json.dumps({'status': 'success', 'data': data})
    except InputValidationError as e:
        return json.dumps({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    sample_input = {'username': 'Player1', 'age': 15, 'email': 'player1@example.com'}
    print(process_data(sample_input))
    invalid_input = {'username': 'Player2', 'age': -3}
    print(process_data(invalid_input))
