from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] and (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'userexists':'Username already taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

        else:
            pw_error = 'Password error'
            return render(request, 'accounts/signup.html', {'pw_error':pw_error})

    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request, 'accounts/login.html', {'badlogin': 'Bad Login'})

    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
