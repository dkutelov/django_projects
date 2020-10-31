from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from user_app.forms import UserLoginForm, UserSignupForm


def user_signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html', {'form': UserSignupForm()})

    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'user/signup.html',
                          {'form': UserSignupForm(),
                           'error': 'Passwords did not match!'})

        try:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            login(request, user)
            return redirect('index')

        except IntegrityError:
            return render(request, 'user/signup.html',
                          {'form': UserSignupForm(),
                           'error': 'This username was already taken!'})


def user_login(request):
    template = 'user/login.html'

    if request.method == 'GET':
        return render(request, template, {'form': UserLoginForm()})

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, template, {
                'form': UserLoginForm(),
                'error': 'Incorrect username or password!'
            })

        login(request, user)
        return redirect('index')


@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
