from functools import wraps
from colorama import Fore

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return Fore.RED + "Contact not found. Please provide a valid name."
        except IndexError:
            return Fore.RED + "Please provide the correct number of arguments."
        except ValueError as value_error:
            return str(value_error)
        except Exception as error:
            return str(error)

    return wrapper
