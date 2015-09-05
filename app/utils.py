from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from bs4 import BeautifulSoup

def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django Rest Framework that adds
    the `status_code` to the response and renames the `detail` key to `error`.
    """
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        if 'detail' in response.data:
            response.data['error'] = response.data['detail']
            del response.data['detail']

    if response is None:
        data = {
        'status_code':500,
        'error' : 'Service temporarily unavailable, try again later.'
        }
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response

def get_summary(html):
    """
    Convert html to plain text and trimmed content length
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()
