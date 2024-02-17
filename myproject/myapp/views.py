# myapp/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def welcome(request):
    return render(request, 'registration/welcome.html')
