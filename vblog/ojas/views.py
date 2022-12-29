from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import SingUpForm,contact,EmpForm
from django.contrib import messages
from .models import Employee
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash

from datetime import timedelta,datetime

# Create your views here.
def signup(request):
    if request.method=='POST':
        fm=SingUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'ypur singup successfully')
            fm=SingUpForm()
    else:
        fm=SingUpForm()


    return render(request,'signup.html',{'form':fm})


# def logins(request):
#     if not request.user.is_authenticated:
#         if request.method=='POST':
#             fm=AuthenticationForm(request=request,data=request.POST)
#             if fm.is_valid():
#                 name = fm.cleaned_data['username']
#                 paswd = fm.cleaned_data['password']
#                 user = authenticate(username=name,password=paswd)
#
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request,'your login seccessfuly')
#                     #return HttpResponseRedirect('/profile/')
#         else:
#             fm=AuthenticationForm()
        #return render(request,'login.html',{'form':fm})
    #else:
       # return HttpResponseRedirect('/profile/')
def profile(request):
    return render(request,'profile.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
       return HttpResponseRedirect('/profile/')


def user_loguot(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def feedback(request):
    return render(request,'feedback.html')


def home(request):
    form=Employee.objects.all()
    return render(request,'home.html',{'form':form})
def about(request):
    return render(request,'about.html')
def Contact(request):
    if request.method=='POST':
        fm=contact(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'successfully aploded')
            return HttpResponse('Thanks')
    else:
        fm=contact()
    return render(request,'contact.html',{'form':fm})

def dashborad(request):
    if request.method=='POST':
        fm=EmpForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=EmpForm()
    else:
        fm=EmpForm()
    return render(request,'dashboard.html',{'form':fm})

def delet(request,id):
    fm=Employee.objects.get(pk=id)
    fm.delete()
    return HttpResponseRedirect('/')

def edite(request, id):
    fm=Employee.objects.get(pk=id)
    form=EmpForm(instance=fm)
    if request.method=='POST':
        form=EmpForm(request.POST,instance=fm)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,'edit.html',{'form':form})

'''
def setcookie(request):
    response = render(request,'set.html')
    response.set_cookie('name','ojas',max_age=20)
    return response

def getcookie(request):
    name = request.COOKIES.get('name','guest')
    return render(request,'get.html',{'name':name})

def delcookie(request):
    response = render(request,'del.html')
    response.del_cookie('name')
    return response

'''

def setcookie(request):
 reponse = render(request, 'set.html')
 reponse.set_signed_cookie('name', 'Alex', salt='aaa', expires=datetime.utcnow()+timedelta(days=2))
 return reponse

def getcookie(request):
 name = request.get_signed_cookie('name', default="Siri", salt='aaa')
 return render(request, 'get.html', {'name':name})

def delcookie(request):
 reponse = render(request, 'del.html')
 reponse.delete_cookie('name')
 return reponse


def setsession(request):
 request.session['name'] = 'Alex'
 request.session['sname'] = 'John'
 return render(request, 'setsession.html')

def getsession(request):
 name = request.session.get('name')
 sname = request.session.get('sname')
 keys = request.session.keys()
 items = request.session.items()
 return render(request, 'getsession.html', {'name':name, 'sname':sname,'keys':keys, 'items':items})

def delsession(request):
# if 'name' in request.session:
 # del request.session['name']
 request.session.flush()
 return render(request, 'delsession.html')