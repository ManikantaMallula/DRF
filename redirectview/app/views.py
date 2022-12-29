from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class ojasRedirectView(RedirectView):
    url = 'https://google.com/'


class newRedirectView(RedirectView):
    pattern_name = 'mindex'
    permanent = True
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk'] = 10
        return super().get_redirect_url(*args, **kwargs)