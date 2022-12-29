from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    send_mail(
        'Testing Mail',
        'Here is the message.',
        'mani.mallula@gmail.com',
        ['vadeppa1994@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse('email sent succussfully')