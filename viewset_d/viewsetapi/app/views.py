from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import Nameserializer


class Testviewset(ViewSet):
    def list(self, request):
        colors = ['red', 'green', 'black']
        return Response({'msg':'happy new year', 'colors':colors})

    def create(self,request):
        serializer = Nameserializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {} happy new year'.format(name)
            return Response({'msg':msg})

        else:
            return Response(serializer.error, status=400)
