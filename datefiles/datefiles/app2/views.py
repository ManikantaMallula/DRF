from django.shortcuts import render

# Create your views here.
from datetime import *
def func2(request):
    td=datetime.now()
    c={"d":td}
    return render(request,'test2.html',c)
