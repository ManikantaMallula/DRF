# def middlewarefunc(get_response):
#     print('printing from middleware function')
#
#     def func1(request):
#         print('printing before view execution')
#
#         response = get_response(request)
#
#
#         print('printing after view execution')
#
#         return response
#     return func1


class Middlewarefunc:
    def __init__(self,get_response):

        self.get_response = get_response
        print('printing from middleware function')

    def __call__(self,request):
        print('printing before view execution')

        response = self.get_response(request)
        print('printing after view execution')

        return response

class Middlewarefunc2:
    def __init__(self,get_response):
        self.get_response = get_response
        print('printing from middleware function2')

    def __call__(self,request):

        print('printing before view execution2')

        response = self.get_response(request)
        print('printing after view execution2')

        return response

class Middlewarefunc3:
    def __init__(self,get_response):
        print('printing from middleware function3')
        self.get_response = get_response

    def __call__(self,request):
        print('printing before view execution3')

        response = self.get_response(request)
        print('printing after view execution3')

        return response













