from django.shortcuts import render
from .models import Manager
from django.db.models import Q
from django.db.models import Avg, Sum, Min, Max, Count


def home(request):
    a=Manager.objects.all()
    #a = Manager.objects.filter(id=1)
    #a = Manager.objects.exclude(id=5)
    #a = Manager.objects.order_by('name')
    #a = Manager.objects.order_by('sal')
    #a = Manager.objects.order_by('sal').reverse()
    #a = Manager.objects.order_by('sal').reverse()[1:4]
    #a = Manager.objects.values()
    #a = Manager.objects.values('name','sal')
    #a = Manager.objects.values('id','loc')
    #a = Manager.objects.values_list('name','loc')
    #a = Manager.objects.using('default')

    #a = Manager.objects.filter(id=22070,name='vadeppa')
    #a = Manager.objects.filter(Q(id=22050)& Q(name='sravani'))
    #a = Manager.objects.filter(Q(id=22070)| Q(name='sravani'))


    #a = Manager.objects.create(name='Vadeppa', id=22070, joindate='2021-11-10', sal=50000, loc='hyd', commi=1500)
    #a = Manager.objects.all()
    #a = Manager.objects.latest('name')
    #a = Manager.objects.filter(id=22092).update(name='prudvi')
    #a = Manager.objects.filter(id=22092).delete()

    #a = Manager.objects.filter(name__exact='vadeppa')
    #a = Manager.objects.filter(name__iexact='vadeppa')
    #a = Manager.objects.filter(name__contains='v')
    #a = Manager.objects.filter(name__contains='S')
    #a = Manager.objects.filter(name__startswith='R')
    #a = Manager.objects.filter(name__istartswith='R')
    #a = Manager.objects.filter(name__endswith='i')
    #a = Manager.objects.filter(name__endswith='i')
    #a = Manager.objects.filter(joindate__year=2022)
    #a = Manager.objects.filter(joindate__month=10)

    #a = Manager.objects.aggregate(Avg('sal'))
    #a = Manager.objects.aggregate(Sum('sal'))
    #a = Manager.objects.aggregate(Min('sal'))
    #a = Manager.objects.aggregate(Avg('sal'))
    #a = Manager.objects.aggregate(Count('sal'))

    #a = Manager.objects.all()[:4]
    #a = Manager.objects.all()[2:4]
    #a = Manager.objects.all()[:4:2]

    return render(request, 'home.html', {"a":a})