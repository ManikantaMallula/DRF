from django.shortcuts import render

# Create your views here.
from datetime import *

def func3(request):
    td=datetime.now()
    c={'d':td}
    return render(request,'test3.html',c)