from src.decorators import input_error


@input_error
def hello_command():
    return "Hello! How can I help you?"
