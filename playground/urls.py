from django.contrib import admin
from django.urls import path
from playground import views

urlpatterns = [
   path("", views.index, name= 'home' ),
   path("hotel", views.hotel, name= 'hotel' ),
   path("tour", views.tour, name= 'tour' ),
   path("car", views.car, name= 'car' ),
   path("signup", views.handlesignup, name= 'handlesignup' ),
   path("login", views.handlelogin, name= 'handlelogin' ),
   path("logout", views.handlelogout, name= 'handlelogout' ),
   path("car_booking", views.car_booking, name='carbooking'),
   path("hotel_booking", views.hotel_booking, name='hotelbooking'),
   path("tour_booking", views.tour_booking, name='tourbooking'),

]
