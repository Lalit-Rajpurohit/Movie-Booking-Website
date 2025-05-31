from django.shortcuts import render , redirect
from .forms import *
from home.models import *
# Create your views here.
from django.contrib import messages

from django.contrib.auth import authenticate ,login



def  adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.error(request,"Account Not Found")
            return render(request,'adminlog.html')

        user_obj = authenticate(username=username,password=password)
        
        if user_obj and user_obj.is_superuser:
            login(request,user_obj)
            return redirect('dash')
        else:
            messages.error(request,"Incoorect Password")
            return render(request,'adminlog.html')
            
    
    
    return render(request,'adminlog.html')


def dashboard(request):
    return render(request,'dashboard.html')

def movie(request):
   
   
    mov = Movie.objects.all()
    context = {'mov':mov}
    return render(request,'mov.html',context)



def theat(request):
    the = Theater.objects.all()

    context = {'the':the}

    return render(request,'the.html',context)

def show(request):
    theaters = Theater.objects.all()
    date = Date.objects.all()
    showtimes = Showtimes.objects.all()
    time  = Time.objects.all()    

    context = {'theaters':theaters,'date':date,'showtimes':showtimes,'time':time}
    return render(request,'show.html',context)

def book(request):
    booking = Booking.objects.all().order_by('-id')
    
    pr = 0

    for book in booking:
        pr += int(book.total)
    
    
    context = {'booking':booking,'price':pr}
    
    return render(request,'bookadmin.html',context)

