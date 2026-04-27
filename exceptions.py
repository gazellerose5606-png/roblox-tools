class RobloxError(Exception):
    pass

class InvalidInputError(RobloxError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(RobloxError):
    def __init__(self, resource_type, resource_id):
        self.message = f'{resource_type} with ID {resource_id} not found.'
        super().__init__(self.message)

class PermissionDeniedError(RobloxError):
    def __init__(self, action):
        self.message = f'Permission denied for action: {action}'
        super().__init__(self.message)

class NetworkError(RobloxError):
    def __init__(self, original_exception):
        self.message = f'Network error occurred: {original_exception}'
        super().__init__(self.message)

class ValidationError(RobloxError):
    def __init__(self, errors):
        self.errors = errors
        self.message = 'Validation failed.'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} Errors: {self.errors}'