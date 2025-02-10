from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def signup(request):
     if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return render(request, 'signup.html')

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            return render(request, 'signup.html')

        else: 
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
            user.save();
            print('User created')
            return redirect('homepage')
     else:
         return render(request, 'signup.html')

def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
   
        user = auth.authenticate(username=username, password=password)
        if user is not None:
             auth.login(request, user)
             return redirect('homepage')
         
        else:
             messages.info(request, 'invalid credentials')
             return render(request, 'login.html')

     else:
        return render(request, 'login.html')
   


def logout(request):
    auth.logout(request)
    return redirect('')    