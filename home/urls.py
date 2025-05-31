from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<id>/',views.movie_page,name='movie'),
    path('theater/<id>/<did>/',views.theater_page,name='theater'),
    path('seat/<int:id>',views.seat_page,name='seat'),
    path('book/',views.book,name='book'),
    path('history/',views.history,name='history'),
    path('about/',views.about,name='about'),
    path('login/',views.login_process,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.lout,name='logout'),
    path('mail/<id>/',views.mail,name='mail'),
   
]