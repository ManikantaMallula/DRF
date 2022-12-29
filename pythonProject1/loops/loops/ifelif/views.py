
from django.shortcuts import render

# Create your views here.

def func(request):
    a="eshwar"
    b=range(1,11)
    c=2
    e=5
    d={'x':a,'y':b,'z':c,'w':e}
    return render(request,'test.html',d)