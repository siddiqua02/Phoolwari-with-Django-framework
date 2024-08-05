from django.shortcuts import render,redirect
from django.contrib.auth.models import User # User Model
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from user.models import Address
# from .models import Flower 

# Create your views here.
def signup(request):
    
    if request.method == "POST":
        messages.error(request, "")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # print(first_name, last_name, username, email, password)
        user_exists = False
        if User.objects.filter(username=username).exists():
            # print("username is already taken")
            messages.error(request, "Username is already taken. try with a new username")
            user_exists = True
        else:
            messages.error(request, "")
        
        if User.objects.filter(email=email).exists():
            # print("Email is already taken")
            messages.error(request, "Email is already taken. try with a new one")
            user_exists = True
        else:
            messages.error(request, "")

        if user_exists:
            return render(request, 'user/signup.html')
        
        user = User.objects.create_user(
           first_name=first_name, 
           last_name=last_name, 
           email=email, 
           username=username, 
           password=password
        )
        user.save()
        messages.success(request, "Account Created Successfully. Login to Continue")

    return render(request, 'user/signup.html')

def signin(request):
    # if request.user.is_authenticated:
    #     return render(request,'page/all_flowers.html')
    if request.method== "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Username or password")
            return render(request,'user/signin.html')
        else:
            login(request,user)
            return redirect('index')
    return render(request,'user/signin.html')
@login_required(login_url='/user/signin')
def signout(request):
    logout(request)
    return render(request, 'user/signin.html')

def add_address(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        house_address=request.POST.get('house_address')
        street_address=request.POST.get('street_address')
        landmark=request.POST.get('landmark')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        zip=request.POST.get('zip')
        mobile=request.POST.get('mobile')
        
        address=Address(
            user=request.user,
            full_name=full_name,
            house_address=house_address,
            street_address=street_address,
            landmark=landmark,
            city=city,
            state=state,
            country=country,
            zip=zip,
            mobile=mobile
            
        )
        print(address)
        address.save()
    return redirect('check_out')