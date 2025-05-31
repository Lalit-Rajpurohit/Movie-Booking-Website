from .models import *
import datetime
import random


#startdate = datetime.date(2024,9,16)
#enddate = datetime.date(2024,9,20)
#date_of_range = [startdate + datetime.timedelta(days=delta) for delta in range((enddate-startdate).days+1)]

#time = [datetime.time(7,00,00),datetime.time(11,00,00),datetime.time(13,00,00),datetime.time(15,00,00),datetime.time(18,00,00),datetime.time(20,00,00),datetime.time(22,00,00)]

def create():
    for m in Movie.objects.all():
        for th in Theater.objects.all():
            for day in Date.objects.all():
                for tm in Time.objects.all():
                    s = random.randrange(1,9)
                    screen = "AUDI " + str(s)
                    seatprice = random.randrange(200,801)
                    
                    showtime = Showtimes.objects.create(theater=th, movie=m,show_date=day,show_time=tm,screen=screen,st=True,seatprice=seatprice)
                    showtime.save()
                    for i in range(0,58):
                        Seat.objects.create(showtime = showtime,seat_number = i,is_available = True).save()
                        showtime.st = True
                        showtime.save()
                    
                    
def delt():
    for show in Showtimes.objects.all():
        show.delete()


def seat():
    for show in Showtimes.objects.all():
        for i in range(0,46):
            Seat.objects.create(showtime = show,seat_number = i,is_available = True).save()

def sc(show):
     for i in range(0,58):
            Seat.objects.create(showtime = show,seat_number = i,is_available = True).save()
            show.st = True
            show.save()
            
            
def like():
    for mov in Movie.objects.all():
        mov.like = int(random.randrange(85,100))
        mov.save()
        


        