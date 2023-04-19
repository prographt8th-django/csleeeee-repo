from rest_framework.exceptions import APIException


class OnlyCache(APIException):
    status_code = 400
    default_detail = "I used redis cache, so I souldn't change it"
