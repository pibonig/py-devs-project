from functools import wraps
from colorama import Fore

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as key_error:
            return f"KeyError: {key_error}"
        except IndexError as index_error:
            return f"IndexError: {index_error}"
        except ValueError as value_error:
            return f"ValueError: {value_error}"
        except Exception as error:
            return f"An error occurred: {error}"

    return wrapper
