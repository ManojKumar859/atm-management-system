from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
def g(request):
    return render(request,"a.html")
def home(request):
    #r=users.objects.filter(userid=request.user)
    #print(list(r))
    return render(request,"b.html")
def profile(request):
    r=users.objects.filter(userid=request.user)
    p=(r.values_list())
    return render(request,"c.html",{"r":r.values_list()})
def ath(request):
    g=Atm.objects.all()
    h=g.values_list()
    k=[]

    for i in h:
        k.append(i[len(i)-1])
    return render(request,"j.html",{"k":k})
def m(request,atm):
    y=Atm.objects.filter(location=atm)
    h=y.values_list()
    j=int(h[0][1])
    #print(h)
    loc=h[0][3]
    u=users.objects.filter(userid=request.user)
    f=u.values_list()
    #print(f)
    g=int(f[0][3])
    if request.method=="POST":
        f=request.POST["k"]
        f=int(f)
        if j<=1000:
            email=EmailMessage("the atm which is present at"+"  "+str(loc.upper())+" "+"is out of cash","the cash at this atm is very less such that it cant satisfy the user requirements so please deposit cash in it asap",settings.EMAIL_HOST_USER,["enter admin mail here"],)
            email.fail_silently=False
            email.send()
        if (f > g):
            print("the amount you entered is not suuficient balance")
            return render(request,"m.html",{"h":"the amount you entered is not suuficient balance"})
        if (f > j):
            print("no amount in atm move to another")
            return render(request,"m.html",{"h":"no amount in atm move to another"})
        if f<g and f<j:
            ats=j-int(f)
            uats=g-int(f)
            y.update(available=ats)
            u.update(cash=uats)
            print(y)
            print(u)
            print("transaction success")
            return redirect("h")
    return render(request,"d.html",{"g":g,"j":j,"loc":loc})




