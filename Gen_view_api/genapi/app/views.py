from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView, FormView
from django.urls import reverse_lazy
from .models import Student
from .forms import Studentform


class Listing(ListView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        model = Student.objects.all()
        return render(request, 'home.html', {'model': model})


class FormTopic(ListView):
    def get(self, request):
        form = Studentform
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
        # model = Student.objects.create(request.POST)
        return HttpResponseRedirect('/')