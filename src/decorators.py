from functools import wraps

from src.response.string_response import StringResponse


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return StringResponse("Contact not found. Please provide a valid name.")
        except IndexError:
            return StringResponse("Please provide the correct number of arguments.")
        except ValueError as value_error:
            return StringResponse(str(value_error))
        except Exception as error:
            return StringResponse(str(error))

    return wrapper
