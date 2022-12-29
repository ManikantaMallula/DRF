from django.shortcuts import render,HttpResponse
from django.views import View
from . forms import Student

# Create your views here.
def home(request):
    return render(request,'home.html')

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
    
    
def aboutfun(request):
    context = {'msg': 'Function Based View'}
    return render(request, 'about.html', context)

class AboutClassView(View):
    def get(self, request):
        context = {'msg': 'Class based Views'}
        return render(request, 'about.html', context)
    
def contactfun(request):
    if request.method=='POST':
        fm=Student(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
    else:
        fm=Student()
    return render(request, 'contact.html', {'form':fm})

class ContactView(View):
    def get(self,request):
        fm=Student()
        return render(request, 'contact.html', {'form':fm})
    
    def post(self,request):
        fm=Student()
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
            

def newsfun(request, template_name):
    template_name = template_name
    context = {'info':'function view'}
    return render(request, template_name, context)

class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info':'class view'}
        return render(request, self.template_name, context)