import logging
from django.utils import timezone
from django.http import HttpResponseForbidden,HttpResponseBadRequest
from django.core.cache import cache
from django.http import HttpResponse,HttpResponseServerError

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

def checkmiddle4(get_response):
    def middleware4(request):
        if request.method == 'GET':
            print("+++++++++++come")
            cached_response = cache.get(request.path)
            print(cached_response)
            if cached_response:
                print("cache yes")
                return cached_response
        response = get_response(request)

        print(response)
        if request.method == 'GET' and response.status_code == 200:
            print("200")
            cache.set(request.path, response, timeout=30)
        return response

    return middleware4

def checkmiddle5(get_response):
    def middleware5(request):
        response = get_response(request)
        text_content = response.content.decode('utf-8')
        modified_response = HttpResponse(f'This is modified text {text_content}', content_type='text/html')
        return modified_response
    return middleware5

def checkmiddle6(get_response):
    def middleware6(request):
        try:
            response = get_response(request)
        except Exception as e:
            logger.exception('An error occurred:')
            return HttpResponseServerError('An error occurred. Please try again later.', status=500)
        
        return response

    return middleware6