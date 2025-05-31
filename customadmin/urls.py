from django.urls import path
from . import views
urlpatterns = [
    path('dash/',views.dashboard,name='dash'),
    path('mov/',views.movie,name='movieadmin'),
    path('the/',views.theat,name='theadmin'),
    path('show/',views.show,name='showadmin'),
    path('booker/',views.book,name='bookadmin'),
    path('adminlogin/',views.adminlogin,name='adminlogin')
]