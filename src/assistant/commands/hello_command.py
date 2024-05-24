from src.decorators import input_error
from src.response.base_response import BaseResponse


@input_error
def hello_command():
    print('Hello! How can I help you?')
