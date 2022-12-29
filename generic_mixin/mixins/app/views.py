from django.shortcuts import render
from .models import Employee
from .serializers import StudentSerializer
from rest_framework import mixins
from rest_framework import generics


class Studentlist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
