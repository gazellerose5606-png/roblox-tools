class RobloxError(Exception):
    pass

class NotFoundError(RobloxError):
    def __init__(self, message="Resource not found."):
        self.message = message
        super().__init__(self.message)

class InvalidParameterError(RobloxError):
    def __init__(self, param, message="Invalid parameter passed."):
        self.param = param
        self.message = f"{message} Parameter: {self.param}"
        super().__init__(self.message)

class PermissionError(RobloxError):
    def __init__(self, message="Insufficient permissions."):
        self.message = message
        super().__init__(self.message)