from django.shortcuts import render

# Create your views here.
def func(request):
    name="Ojas"
    sentense="happy new year"
    lis=[1,2,3,4,5,6,7,8]
    paragraph="happy new year abc def ghi jkl mnop qrst uvwxyz "
    de=""
    details={"na":name,"sen":sentense,"l":lis,"p":paragraph,"d":""}
    return render(request,"test.html",details)


