import logging
from django.utils import timezone
from django.http import HttpResponseForbidden,HttpResponseBadRequest


logger = logging.getLogger(__name__)
request_counts = {}

def checkmiddle1(get_response):
    def middleware1(request):
        logger.info(
            f"User {request.META.get('REMOTE_ADDR')} accessed {request.method} {request.path} at {timezone.now()}"
        )
        response = get_response(request)
        return response
    return middleware1

def checkmiddle2(get_response):
    def middleware2(request):
        ip_address = request.META.get('REMOTE_ADDR')
        request_counts[ip_address] = request_counts.get(ip_address, 0) + 1
        if request_counts[ip_address] > 25:
            return HttpResponseForbidden("Rate limit exceeded. Please try again later.")
        response = get_response(request)
        return response

    return middleware2

def checkmiddle3(get_response):
    def middleware3(request):
        if request.path.startswith('/auth'):
            print("inside auth")
            if 'Authorization' not in request.headers:
                return HttpResponseBadRequest('Authorization header is required.')
            
        response = get_response(request)
        return response

    return middleware3