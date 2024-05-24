from src.decorators import input_error
from src.response.base_response import BaseResponse
from src.response.string_response import StringResponse


@input_error
def hello_command() -> BaseResponse:
    return StringResponse('Hello! How can I help you?')
