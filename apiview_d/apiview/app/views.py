from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Nameserializer

class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = ['red', 'blue', 'black', 'green']
        return Response({'msg':'Happy new year','data':data})

    def post(self, request):
        serializer = Nameserializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'hello{},happy new year'.format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request):
        return Response({'msg':'this response from put method'})

    def patch(self, request):
        return Response({'msg':'this response from put method'})

    def delete(self, request):
        return Response({'msg':'this response from put method'})


