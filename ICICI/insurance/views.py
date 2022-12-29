from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .models import Route, BusDetails, Destination, Customer
from .forms import RouteForm, CustomerForm
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = RouteForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = RouteForm()
            request.session['route'] = request.POST
            return HttpResponseRedirect('/buslist/')
    else:
        fm = RouteForm()
    return render(request, 'home.html', {'form': fm})


def buslist(request):
   # print(request.session['route'])
    destination = request.session['route']['destination_two']
    buses = BusDetails.objects.all()

    if request.method == "POST":
        return HttpResponseRedirect('/customer/')
    print(destination,'..........................')
    return render(request, 'buslist.html', {'buses': buses, 'destination': int(destination)})

def customer(request):
    request.session['customer'] = request.POST

    busd = BusDetails.objects.all()
    if request.method == 'POST':

        fm = CustomerForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = CustomerForm()
            return HttpResponseRedirect('/confirm/')
    else:
        fm = CustomerForm()
    return render(request, 'customer.html',{'form':fm})

def confirm(request):
    cust = request.session['customer']
    bus = BusDetails.objects.all()
    d = dict()
    l=[]
    l2 = ['bus name - ', 'source - ', 'destination - ', 'start time - ', 'arrival time - ', 'price - ' ]

    for i in bus:
        if int(i.id) == int(cust['bus_name']):
            print(i.destination_one)
            l.append(i.bus_name)
            l.append(i.source)
            l.append(i.destination_one)
            l.append(i.start_time)
            l.append(i.arrival_time)
            l.append(i.price)

    print(l,'............')
    print(l2)

    for k in l:
        for m in l2:
            if k!=m:
                d[m]=k

    print(d)

    return render(request, 'confirm.html', {'cust': cust,'l':l, "l2":l2, 'bus':bus})




def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'profile.html')


def User_SignUp(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            Email = fm.cleaned_data['email']
            messages.success(request, 'Successfully Registered')
            send_mail(' Registration Successfull',
                      'Signup and Registration Was Successfull Congratulations Now You can read and Write Blogs On My Website.',
                      'priyakota44@gmail.com', [str(Email)], fail_silently=False)
            print("Form is Validated...")
            print("Email sent was SuccessFull...")
            fm.save()

            return HttpResponseRedirect('/home/home')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {"form": fm})


def User_Login(request):
    print(request.user)
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                un = fm.cleaned_data['username']
                up = fm.cleaned_data['password']
                user = authenticate(username=un, password=up)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')

                    return HttpResponseRedirect('/home/profile')

        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {"form": fm})
    else:
        return HttpResponseRedirect('/home/home')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect('/home/home')
    return render(request, 'logout.html')


def payment(request):
    if request.method == 'POST':
        import razorpay
        amount = 5000,
        currency: "INR"
        client = razorpay.Client(auth=("rzp_test_mPNVIRhRiNsUb5", "QZn4mjNTyuugEH1agYwUiIx9"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    return render(request, 'payment.html')


@csrf_exempt
def success(request):
    return render(request, 'success.html')



