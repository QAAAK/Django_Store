from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from  django.urls import reverse

from user.models import User
from user.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': UserLoginForm}
    return render(request, 'user/login.html', context)
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': UserRegistrationForm}
    return render(request, 'user/register.html', context)
