import re

class InputValidator:
    @staticmethod
    def is_valid_username(username):
        return isinstance(username, str) and 3 <= len(username) <= 20 and re.match("^[a-zA-Z0-9_]*$, username)

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 13 <= age <= 150

    @staticmethod
    def is_valid_email(email):
        return isinstance(email, str) and re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

class MainProcessor:
    def process_input(self, username, age, email):
        if not InputValidator.is_valid_username(username):
            raise ValueError('Invalid username')
        if not InputValidator.is_valid_age(age):
            raise ValueError('Invalid age')
        if not InputValidator.is_valid_email(email):
            raise ValueError('Invalid email')
        # Proceed with processing
        print('Input is valid')

if __name__ == '__main__':
    processor = MainProcessor()
    try:
        processor.process_input('user_example', 25, 'user@example.com')
    except ValueError as e:
        print(e)