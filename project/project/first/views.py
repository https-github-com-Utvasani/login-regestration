from django.shortcuts import render
from django.http import HttpResponse
from first.models import Registration
# Create your views here.
def index(request):
    return render(request,'index.html')
def registration(request):
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('password'):
            saverecord=Registration()
            saverecord.username=request.POST.get('username')
            saverecord.email=request.POST.get('email')
            saverecord.password=request.POST.get('password')
            saverecord.save()
            return HttpResponse("good")
        else:
            return HttpResponse("bad")
    else:
        pass
def login(request):
    return HttpResponse("Login")