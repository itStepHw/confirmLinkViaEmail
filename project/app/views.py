from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

from functools import wraps

import random
import string


def generate_random_string(length=20):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def user_is_verified(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_verified:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('index')

    return _wrapped_view


@user_is_verified
def profile(request):
    return render(request, 'app/profile.html')


def registration(request):
    regForm = RegisetrForm()

    if request.method == 'POST':
        regForm = RegisetrForm(request.POST)
        if regForm.is_valid():
            temp = regForm.save(commit=False)
            temp.verify_code = generate_random_string()

            email = EmailMessage(
                subject='verification code',
                body=f'http://127.0.0.1:8000/verify/?code={temp.verify_code}',
                to=[temp.email],
            )
            email.send()

            temp.save()
            return redirect('index')

    context = {'regForm': regForm}

    return render(request, 'app/registration.html', context)


def index(request):
    return render(request, 'app/index.html')


def signIn(request):
    signInForm = SignInForm()
    if request.method == 'POST':
        signInForm = SignInForm(request.POST)
        print('1')
        if signInForm.is_valid():
            print('2')
            username = signInForm.cleaned_data['username']
            password = signInForm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                print('3')
                login(request, user)
                return redirect('index')

    context = {'signInForm': signInForm}
    return render(request, 'app/sign.html', context)


def verifyUser(request):
    code = request.GET['code']
    user = get_object_or_404(MyUser, verify_code=code)
    if user:
        user.verify_code = ''
        user.is_verified = True
        user.save()
        return redirect('index')


def logoutUser(request):
    logout(request)
    return redirect('index')
