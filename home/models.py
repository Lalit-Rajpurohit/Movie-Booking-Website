from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Theater(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=155)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Star(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='stars',blank=True,null=True)

    def __str__(self):
        return self.name
    

class TypeMov(models.Model):
    Typ = models.CharField(max_length=25)
    
    def __str__(self):
        return self.Typ

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    tralier = models.CharField(max_length=300,null=True,blank=True)
    poster = models.ImageField(upload_to='movie_posters',blank=True,null=True)
    banner = models.ImageField(upload_to='movie_posters',blank=True,null=True)
    star = models.ManyToManyField(Star)
    typ = models.ManyToManyField(TypeMov)
    satus = models.BooleanField(default=True)
    like = models.IntegerField(default=92)

    def __str__(self):
        return self.title

class Date(models.Model):
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)

class Time(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)
    

class Showtimes(models.Model):
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name="theater")
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="movie")
    show_date = models.ForeignKey(Date,on_delete=models.CASCADE,related_name="day",null=True)
    show_time = models.ForeignKey(Time,on_delete=models.CASCADE,related_name="stime",null=True)
    screen = models.CharField(max_length=20,default="AUDI 01",null=True,blank=True)
    st = models.BooleanField(default=True)
    seatprice = models.IntegerField(default=200)

    def __str__(self):
        return f"{self.movie} at {self.theater}__ {str(self.show_date)}__{str(self.show_time)}"

class Seat(models.Model):
    showtime = models.ForeignKey(Showtimes,on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Seat{self.seat_number}"

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    showtimes = models.ForeignKey(Showtimes,on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.CharField(max_length=20, default='100')
    qr = models.ImageField(upload_to='qrcode',null=True)
    BID = models.CharField(max_length=26,null=True,blank=True)
    BNO = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f"Booking for {self.showtimes}" 
    
    