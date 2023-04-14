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

        if response.status_code == 500:
            response = get_response(
                message="Internal server error",
                status_code=response.status_code
            )

        if response.status_code == 200:
            response = get_response(
                message="Success",
                result=response.data,
                status_code=response.status_code
            )
            return JsonResponse(response, status=response['status_code'])
        
        if response.status_code == 201:
            response = get_response(
                message="Created",
                result=response.data,
                status_code=response.status_code
            )
            return JsonResponse(response, status=response['status_code'])
            

        return response
