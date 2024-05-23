from src.decorators import input_error


@input_error
def hello_command():
    print('Hello! How can I help you?')
