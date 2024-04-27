from django.shortcuts import render, HttpResponse
from Myapp.models import Cookie
# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("Index Page")

#Database
def saveCookie(request):
    if request.method =="POST":
        Name=request.POST['Name']
        Email=request.POST['Email']
        Phone=request.POST['Phone']
        new_Cookie=Cookie(Name=Name,Email=Email,Phone=Phone)
        new_Cookie.save()
        return render(request,"index.html")
    else:
        return HttpResponse(request,"Not Connected")
    

# Data of SEMESTER 3
def se3(request):
    return render(request,"se3.html")

def dbms(request):
    return render(request,"dbms.html")

def pcpf(request):
    return render(request,"pcpf.html")

def m3(request):
    return render(request,"M3.html")

def dsa(request):
    return render(request,"dsa.html")

# def cnnd(request):
#     return render(request,"cnnd.html")

#Data for Semester 4

def se4(request):
    return render(request,"se4.html")

def m4(request):
    return render(request,"m4.html")

def at(request):
    return render(request,"at.html")

def coa(request):
    return render(request,"coa.html")

def os(request):
    return render(request,"os.html")

def cnnd(request):
    return render(request,"cnnd.html")
