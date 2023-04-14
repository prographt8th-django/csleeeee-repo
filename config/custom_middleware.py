import json
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def get_response(message="", result={}, status_code=200):
    return {
        "message": message,
        "result": result,
        "status_code": status_code
    }


class RequestResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response
