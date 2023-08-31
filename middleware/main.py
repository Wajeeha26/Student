from typing import Any
from django.http import HttpRequest

class StudentMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest, *args, **kwds) -> Any:
        print('***** This is middleware *****')
        response = self.get_response(request)
        return response
