from functools import wraps


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass

    return wrapper
