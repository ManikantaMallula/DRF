from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'alex'
        context['roll'] = 22076
        # context = {'name':'alex', 'roll':22076}
        print(context)
        print(kwargs)
        return context