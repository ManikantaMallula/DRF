from django.shortcuts import render,HttpResponseRedirect
from .models import modelDis
from .forms import formDis
# Create your views here.
def show(request):
    if request.method == 'POST':
        fm=formDis(request.POST)
        if fm.is_valid():
            n=fm.cleaned_data['name']
            a=fm.cleaned_data['age']

            ob=modelDis(name=n,age=a)
            ob.save()
            fm=formDis()
            ob1=modelDis.objects.all()
            return HttpResponseRedirect('home',{"form":fm,"ob1":ob1})
    else:
        fm=formDis()
    ob1 = modelDis.objects.all()


    return render(request,'home.html',{"form":fm,"ob1":ob1})
