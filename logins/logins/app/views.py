from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import Signup

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def signup(request):
    if request.method == "POST":
        fm=Signup(request.POST)
        if fm.is_valid():
            messages.success(request,'profile created successfully')
            fm.save()

    else:
        fm=Signup()
    return render(request,'signup.html',{'form':fm})

def login(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.user)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname, password=upass)
                fm.save()

                if user is not None:
                    login(request,user)
                    messages.success('logged in successfully ')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})

    else:
        return HttpResponseRedirect('/login/')


def logout(request):

    logout(request)

    return HttpResponseRedirect('/login/')


def cpass1(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success("password changed successfully ")

                return HttpResponseRedirect('profile/')

            else:
                fm=SetPasswordForm(user=request.user)
            return render(request,'cpass1.html',{"form":fm})
        else:
            return HttpResponseRedirect('/login/')



def cpass2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(request=request.user , data=request.POST)
            if fm.is_valid:
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success('password changed successfully ')
                return HttpResponseRedirect('/profile/')


        else:
            fm=SetPasswordForm(request.user)
        return render(request,'cpass2.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')





