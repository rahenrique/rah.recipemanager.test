from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next'] if 'next' in request.POST else None

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next is not None:
                return redirect(next)
            return redirect(reverse('home:home'))
        else:
            return render(request, 'accounts/login.html', {'error': 'The username and password don\'t match'})
    else:
        return render(request, 'accounts/login.html')


def signout(request):
    logout(request)
    return redirect(reverse('home:home'))


def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            _validate_username(username)
            _validate_passwords(password, confirm_password)

            user = User.objects.create_user(username, password=password)
            login(request, user)
            return render(request, 'accounts/signup.html', {'success': 'Account created'})

        except Exception as e:
            return render(request, 'accounts/signup.html', {'error': str(e)})
    else:
        return render(request, 'accounts/signup.html')


def _validate_username(username):
    if User.objects.filter(username=username).exists():
        raise Exception(f'Username \'{username}\' is already taken')


def _validate_passwords(password, confirm_password):
    if password != confirm_password:
        raise Exception('Passwords don\'t match')
