from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        data = request.POST
        if data['password'] == data['confirm_password']:
            if not User.objects.filter(username=data['email']).exists():
                user = User.objects.create_user(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    username=data['email'],
                    email=data['email'],
                    password=data['password']
                )
                return redirect('/user')
            else:
                messages.error(request, "Username already exists.")
        else:
            messages.error(request, "Password do not match.")
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/park/')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/user')