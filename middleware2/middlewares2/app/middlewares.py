from django.shortcuts import HttpResponse


class Process:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process(self, *args, **kwargs):
        print('process before view')
        return HttpResponse("process before view")
    #   return None


class Exception:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def exception(self, request, exception):
        msg = exception
        cname = eception.__class__.__name__
        print(msg)
        print(cname)

        return HttpResponse(mg)


class Templateexp:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def templateexp(self, request, response):
        print('printing from templateexp ')
        response.context_data['name'] = "ojas innovative tech"
        return response
