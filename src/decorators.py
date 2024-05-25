from functools import wraps

from colorama import Fore


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as key_error:
            return Fore.RED + f"KeyError: {key_error}"
        except IndexError as index_error:
            return Fore.RED + f"IndexError: {index_error}"
        except ValueError as value_error:
            return Fore.RED + f"ValueError: {value_error}"
        except Exception as error:
            return Fore.RED + f"An error occurred: {error}"

    return wrapper
