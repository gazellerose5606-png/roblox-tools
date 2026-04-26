class RobloxError(Exception):
    pass

class InvalidParameterError(RobloxError):
    def __init__(self, parameter, message="Invalid parameter provided."):
        self.parameter = parameter
        self.message = message
        super().__init__(self.message)

class NotFoundError(RobloxError):
    def __init__(self, resource, message="Resource not found."):
        self.resource = resource
        self.message = message
        super().__init__(self.message)

class AuthenticationError(RobloxError):
    def __init__(self, message="Authentication failed."):
        self.message = message
        super().__init__(self.message)

class PermissionDeniedError(RobloxError):
    def __init__(self, action, message="Permission denied."):
        self.action = action
        self.message = message
        super().__init__(self.message)

class RateLimitExceededError(RobloxError):
    def __init__(self, limit, message="Rate limit exceeded."):
        self.limit = limit
        self.message = message
        super().__init__(self.message)
