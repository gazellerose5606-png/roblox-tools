class RobloxError(Exception):
    pass

class NotFoundError(RobloxError):
    def __init__(self, message='Resource not found'):  
        super().__init__(message)

class InvalidInputError(RobloxError):
    def __init__(self, message='Invalid input provided'):  
        super().__init__(message)

class PermissionDeniedError(RobloxError):
    def __init__(self, message='Permission denied'):  
        super().__init__(message)

class RateLimitExceededError(RobloxError):
    def __init__(self, message='Rate limit exceeded'):  
        super().__init__(message)

def handle_exception(exception):
    if isinstance(exception, NotFoundError):
        return {'error': 'Not Found', 'message': str(exception)}
    elif isinstance(exception, InvalidInputError):
        return {'error': 'Invalid Input', 'message': str(exception)}
    elif isinstance(exception, PermissionDeniedError):
        return {'error': 'Permission Denied', 'message': str(exception)}
    elif isinstance(exception, RateLimitExceededError):
        return {'error': 'Rate Limit Exceeded', 'message': str(exception)}
    else:
        return {'error': 'Unknown Error', 'message': str(exception)}