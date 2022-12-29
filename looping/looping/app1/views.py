from django.shortcuts import render

# Create your views here.
def func(request):
    a="Ojas"
    b=range(1,11)
    c=5
    e=7
    d={"x":a,"y":b,"z":c,"h":e}
    return render(request,'test.html',d)