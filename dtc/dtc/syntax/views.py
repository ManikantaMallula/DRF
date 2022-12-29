from django.shortcuts import render

# Create your views here.
def func1(request):
    method_name={'mname':"display-method"}
    return render(request,"test1.html",context=method_name)

def func2(request):
    tools={'tls':'dtltools'}
    return render(request,"test2.html",tools)

def func3(request):
    functions={"fun":"dtlfunctions"}
    return render(request,"test3.html",{"fun":"dtlfunctions"})

def func4(request):
    logics={'lgc':'dtllogics'}
    return render(request,"test4.html",logics)

def func5(request):
    library={'lib':'dtllibraries'}
    return render(request,"test5.html",library)