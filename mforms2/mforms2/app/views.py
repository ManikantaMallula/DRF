from django.shortcuts import render
from .forms import StudentRegistration


# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        a = StudentRegistration(request.POST)
        if a.is_valid():
            print('Form Validated')
            print('Name:', a.cleaned_data['name'])
            print('Email:', a.cleaned_data['email'])
            print('Password:', a.cleaned_data['password'])

    else:
        a = StudentRegistration()

    return render(request,'test.html',{'a': a})