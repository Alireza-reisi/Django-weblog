from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def users_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def users_signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('gmail'),
                                        password=request.POST.get('password'))
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html')


def users_logout(request):
    logout(request)
    return redirect('/')
