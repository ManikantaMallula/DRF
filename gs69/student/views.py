from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookie(request):
 reponse = render(request, 'student/setcookie.html')
 reponse.set_signed_cookie('name', 'Sonam', salt='apple', expires=datetime.utcnow()+timedelta(days=2))
 return reponse

def getcookie(request):
 name = request.get_signed_cookie('name', default="Ojas", salt='banana')
 return render(request, 'student/getcookie.html', {'name':name})

def delcookie(request):
 reponse = render(request, 'student/delcookie.html')
 reponse.delete_cookie('name')
 return reponse