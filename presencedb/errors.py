class UserNotFound(BaseException):
    """Raise an Exception when the User is not found"""

class ActivityNotFound(BaseException):
    """Raise an error when an Activity is not found"""

class UnexpectedRequestError(BaseException):
    """Raise an error when an unexpected API error occurs"""