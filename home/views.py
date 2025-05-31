from django.shortcuts import render ,redirect ,HttpResponseRedirect
from .models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.

import qrcode

from django.core.files.images import ImageFile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.utils.html import strip_tags
from .helpers import *


from .utils import sc  


def index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    m1 = Movie.objects.get(title="Dangal")
    ll = ["Dhoom3","Dangal","Padmaavat","PK","KGF"]
    movie = Movie.objects.filter(Q(title="Padmaavat") | Q(title="PK") | Q(title="Dhoom3")| Q(title="KGF") )
    mov = Movie.objects.filter(satus=True) 
    context = {'movies':movie,'m1':m1,'movs':mov}
    return render(request,"index.html",context)

def movie_page(request,id):
    movie = Movie.objects.get(id=id)
    context = {'movies':movie}
    show = Showtimes.objects.all()
    for s in show:
        if s.st == False:
            sc(s)
            
    return render(request,'movie.html',context)

def theater_page(request,id,did=0):
    if did == '0':
        date = Date.objects.first()
    else:
        date = Date.objects.get(id=did)
    time = Time.objects.all()
    theater = Theater.objects.all()
    alldate = Date.objects.all()
    showtimes = Showtimes.objects.filter(movie__id = id)
    s1 = showtimes[0]
    context ={'theaters':theater,'showtimes':showtimes,'day':date,'time':time,'s1':s1,'alldate':alldate}
    return render(request,'theater.html',context)

def seat_page(request,id):
    Showtime = Showtimes.objects.get(id=id)
    seat = Seat.objects.filter(showtime=Showtime)
    if request.method == "POST":
        sb = request.POST.getlist("sb")
        bookseat = []
        price =0
        tax=0
        c=0
        for ss in sb:
            s = Seat.objects.get(id=ss)
            details = s.showtime
            price += s.showtime.seatprice
          
            c += 1
            bookseat.append(s)
        total = price + tax
        context = {'bookseat':bookseat,'details':details,'total':total,'price':price,'tax':tax,'c':c}
        return render(request,'book.html',context)
    context = { 'showtime' : Showtime ,'seat':seat }
  
    return render(request,'seat.html',context)
 
def book(request):
    if request.method == "POST":
        ids = request.POST.getlist('sb')
        total =request.POST.get('total')
        seat = Seat.objects.filter(id__in = ids)
        for s in seat:
            s.is_available = False
            s.save()
    deatils = seat[0].showtime
    sr= f"{deatils.movie.title} {deatils.theater.name} Seat no:"
    for s in seat:
        sr += f"{s.seat_number} , "
    
    bid = genId()
    bno = genNo()
    
    
    booking = Booking.objects.create(user=request.user,showtimes=deatils,total=total,BID=bid,BNO=bno)
    booking.seats.set(seat)
    booking.save()
    
    sr += f' {booking.BID} {booking.BNO} {booking.showtimes.screen}'
    
    qr =qrcode.make(sr)
    
    name = f"{booking.id}.jpg"
    qr.save("C:/code/Zor/movie/public/static/" + name)
    
    n = name.split(".")
    name = n[0]
    
    context = {'booking':booking}
    return render(request,"ticket.html",context)

def history(request):
    booking = Booking.objects.filter(user = request.user)
    context = {'book':booking}
    return render(request,'history.html',context)

def about(request):
    return render(request,"about.html")

def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password=request.POST.get('password')
        cpassword = request.POST.get('cpassword')
	
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request,"Username is already taken")
            return redirect('signup')

        if password != cpassword:
            messages.error(request,"You entered confirm password wrong")
            return redirect('signup')
        else:
             new_user = User.objects.create_user(username,email,password)
             new_user.save()
             messages.success(request,"Account Created! please Login")
             return redirect('login')
    
    return render(request,"signupp.html")



def login_process(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pas=request.POST.get('password')
        user=authenticate(request,username=username,password=pas)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,"Username or Password is Incorrect")
            return redirect('login')

        # print(username,password)
    return render(request,"login.html")


def lout(request):
    logout(request)
    return redirect('index')


def mail(request,id):
    booking = Booking.objects.get(id=int(id))
    
    html_content = render_to_string(
    "tt.html",
    context={'booking':booking},
    )
    user = User.objects.get(id=request.user.id)
    
    plain_message = strip_tags(html_content)
    
    msg = EmailMultiAlternatives(
    subject="Ticket",
    body=plain_message,
    from_email= "gamerzer425@gmail.com",
  to=  [user.email],
    )
    

    # Lastly, attach the HTML content to the email instance and send.
   
   
    

    msg.send()
    
    context = {'booking':booking}
    return render(request,"ticket.html",context)


# message.attach("design.png", img_data, "image/png")
# to=  ["rajpurohitlalit181@gmail.com"],

