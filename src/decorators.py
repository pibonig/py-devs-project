from functools import wraps


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found. Please provide a valid name."
        except IndexError:
            return "Please provide the correct number of arguments."
        except ValueError as value_error:
            return str(value_error)
        except Exception as error:
            return str(error)

    return wrapper
