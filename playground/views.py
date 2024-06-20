from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from playground.models import Post
from playground.models import carbooking
from playground.models import hotelbooking
from playground.models import tourbooking

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hotel(request):
    return render(request, 'hotel.html')

def tour(request):
    return render(request, 'tour.html')

def car(request):
    return render(request, 'car.html')

def handlesignup(request):
    if request.method == "POST":
        #Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1= request.POST['pass1']
        pass2 = request.POST['pass2']        

        # Check for errors
        if len(username) > 10:
            messages.error(request, "Username should be less than 10 characters")
            return redirect('home')
        
        if pass1 != pass2 :
            messages.error(request, "Passwords do not match")
            return redirect('home')
        
        

        # Create the user
        myuser = User.objects.create_user(username, email, pass1) 
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')

    
    else:
        return HttpResponse('404 - Not Found')
    

def handlelogin(request):
    if request.method == "POST":
        #Get the post parameters
        usernamelogin = request.POST['usernamelogin']
        password = request.POST['password']

        user = authenticate(username = usernamelogin, password = password)

        if user is not None: 
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect('home')
        
    return HttpResponse('404 - Not Found')
       
def handlelogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Successfully logged Out")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')
    
def car_booking(request):
    if request.method == "POST":
        #Get the post parameters
        name = request.POST['name']
        days = request.POST['days']
        srno = request.POST['srno']
        phone = request.POST['phone']
        print(name, days, phone, srno)
        booking = carbooking(name = name, days = days, phone = phone, srno = srno)
        booking.save()
        messages.success(request, "Booking Confirmed")
        return redirect('car')
    else:
        return HttpResponse('404 - Not Found')
    
def hotel_booking(request):
    if request.method == "POST":
        #Get the post parameters
        name = request.POST['name']
        night = request.POST['night']
        phone = request.POST['phone']
        srno = request.POST['srno']
        print(name, night, phone, srno)
        booking = hotelbooking(name = name, night = night, phone = phone, srno = srno)
        booking.save()
        messages.success(request, "Booking Confirmed")
        return redirect('hotel')
    else:
        return HttpResponse('404 - Not Found')
    
def tour_booking(request):
    if request.method == "POST":
        #Get the post parameters
        name = request.POST['name']
        person = request.POST['person']
        phone = request.POST['phone']
        srno = request.POST['srno']
        print(name, person, phone, srno)
        booking = tourbooking(name = name, person = person, phone = phone, srno=srno)
        booking.save()
        messages.success(request, "Booking Confirmed")
        return redirect('tour')
    else:
        return HttpResponse('404 - Not Found')

    