from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(Date)
admin.site.register(Time)
admin.site.register(Showtimes)

admin.site.register(Booking)
admin.site.register(Star)
admin.site.register(TypeMov)

