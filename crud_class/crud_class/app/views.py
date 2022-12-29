from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import SignUpForm,Contact,Dashboardform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from .models import Dashboard
from django.core.cache import cache
from datetime import datetime,timedelta
from django.core.mail import send_mail
from django.views.generic.base import RedirectView
from django.views import View

def base(request):
    return render(request,'base.html')

def home(request):
    blogs = Dashboard.objects.all()
    user = request.user
    ct = cache.get('count', version=user.pk)
    ip = request.session.get('ip')
    return render(request, 'home.html', {'crud_class': blogs,'ct':ct,'ip':ip})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        fm = Contact(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thanks for Contacting Us')
            return HttpResponseRedirect("<h1> Succussfull </h1>")
    else:
        fm = Contact()
    return render(request,'contact.html',{'form':fm})

def signup(request):
    if request.method == "POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            EMAIL=fm.cleaned_data['email']
            user=fm.save()
            login(request,user)
            messages.success(request,'Account Created Successfully !!!')
            send_mail(
                'sending mail',
                'sending from django',
                'mani.mallula@gmail.com',
                [str(EMAIL)],
                fail_silently=False
            )
            
    else:
        fm=SignUpForm()
    return render(request,'signup.html',{'form':fm})



def ulogin(request):
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
                return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
       return HttpResponseRedirect('/dashboard/')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def dashboard(request):
    if request.method == "POST":
        fm = Dashboardform(request.POST)
        if fm.is_valid():
            messages.success(request, 'Updated')
            fm.save()
    else:
      fm = Dashboardform()
    return render(request, 'dashboard.html', {'form':fm})

class DeleteView(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwargs):
        del_id=kwargs['id']
        Dashboard.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)
 
class EditView(View):
    def get(self,request,id):
        pi=Dashboard.objects.get(pk=id)
        fm=Dashboardform(instance=pi)
        return render(request, 'edit.html', {'form': fm})
    
    def post(self,request,id):
        pi=Dashboard.objects.get(pk=id)
        fm=Dashboardform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request, 'edit.html', {'form': fm})

def set_Blog_cookies(request):
    response=render(request,'blog_cookie.html')

    response.set_signed_cookie('name','Sonnam',salt='Love',expires=datetime.utcnow()+timedelta(days=2))
    return response

def get_Blog_coookies(request):
    name=request.get_signed_cookie('name',default='Alex',salt='Hello')

    return render(request,'get_blog_cookie.html',{'name':name})

def del_Blog_cookies(request):
    response= render(request,'del_Blog_cookies.html')
    response.delete_cookie('name')
    return response



def set_Blog_session(request):
    request.session['name']='Mounika'
    # request.session['mname']='Yarramasa'
    # request.session.set_expiry(10)
    request.session.set_test_cookie()
    return render(request,'set_session.html')

def get_Blog_session(request):
    name=request.session.get('name')
    print(request.session.test_cookie_worked())
    return render(request, 'get_session.html', {'name': name})

def del_Blog_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'del_session.html')

def excep(request):
    print("I am Excp View")

    print(10/0)
    return HttpResponse("This is Excp Page")

def user(request):
    print("user function")
    context = {'name':'Ojas'}
    return TemplateResponse(request, 'user.html', context)

# def middleware(request):
#     return HttpResponse("view line")





