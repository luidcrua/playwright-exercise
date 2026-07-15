import random
import time

from django.shortcuts import redirect, render

VALID_EMAIL = 'user@test.com'
VALID_PASSWORD = 'password'


def home(request):
    return redirect('/login')


def login(request):
    if request.method == 'POST':
        time.sleep(random.uniform(0, .4))
        if (request.POST.get('email') == VALID_EMAIL
                and request.POST.get('password') == VALID_PASSWORD):
            return redirect('/dashboard')
    return render(request, 'challenge_app/login.html')


def dashboard(request):
    return render(request, 'challenge_app/dashboard.html')
