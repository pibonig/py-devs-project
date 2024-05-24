from src.decorators import input_error


@input_error
def close_command():
    return False
