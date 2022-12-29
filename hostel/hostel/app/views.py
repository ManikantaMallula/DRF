from django.shortcuts import render, HttpResponseRedirect
from .forms import hostelform, hostelform2
from .models import hostel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout


from django.contrib import messages


# Create your views here.

def show(request):
    if request.method == 'POST':
        a = hostelform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['hname']
            cn = a.cleaned_data['cno']
            ad = a.cleaned_data['address']
            reg = hostel(hname=nm, cno=cn, address=ad)
            reg.save()
            messages.debug(request, 'statements were executed')
            messages.info(request, 'info line')
            messages.success(request, "success line")
            messages.warning(request, 'warning line')
            messages.error(request, 'error line')
            a = hostelform()
    else:
        a = hostelform()
    stud = hostel.objects.all()
    return render(request, 'home.html', {'a': a, 'stu': stud})


def edit(request, id):
    if request.method == 'POST':
        pi = hostel.objects.get(pk=id)
        a = hostelform(request.POST, instance=pi)
        if a.is_valid():
            a.save()
    else:
        pi = hostel.objects.get(pk=id)
        a = hostelform(instance=pi)
    return render(request, 'edit.html', {'a': a})


# This Function will Delete
def delete(request, id):
    if request.method == 'POST':
        pi = hostel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


'''
def signup(request):
 if request.method=='POST':
  fm=UserCreationForm(request.POST)
  if fm.is_valid():
   fm.save()

 else:
  fm=UserCreationForm()
 return render(request,'sign.html', {'form':fm})  '''


def signup(request):
    if request.method == "POST":
        fm = hostelform2(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
    else:
        fm = hostelform2()
    return render(request, 'sign.html', {'form': fm})


def userprofile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')


def userlogin(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            if fm.is_valid():
                uname = fm.is_cleaned['username']
                upass = fm.is_cleaned['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {"form": fm})
    else:
        return HttpResponseRedirect('profile')


def logout(request):
    logout(request)
    return HttpResponseRedirect('login')
