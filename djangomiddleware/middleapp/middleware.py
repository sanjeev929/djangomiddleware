def checkmiddle1(get_response):
    print("Creating checkmiddle middleware1")

    def middleware1(request):
        print("Executing middleware1")
        response = get_response(request)
        response['X-Example-Header'] = 'Hello from custom middleware 1!'
        print("last excute1")
        return response

    return middleware1

def checkmiddle2(get_response):
    print("Creating checkmiddle middleware1")

    def middleware2(request):
        print("Executing middleware2")
        response = get_response(request)
        response['X-Example-Header'] = 'Hello from custom middleware 2!'
        print("last excute2")
        return response

    return middleware2