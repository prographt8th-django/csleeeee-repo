def view_process_time_middleware(get_response):
    def middleware(request):
        print("Before response", type(get_response), type(request), flush=True)
        response = get_response(request)
        print("After response", type(response), flush=True)
        return response
    return middleware
