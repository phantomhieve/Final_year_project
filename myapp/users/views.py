from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/register.html', args)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            valid, message = form.login()
            if valid: 
                auth_login(request, message)
                # this is not working idk why
                return render(main)
            else:
                # can redirect with message store in message 
                return redirect(login)
    form = LoginForm()
    args = {'form': form}
    return render(request, 'accounts/login.html', args)

@login_required
def main(request):
    print('Here')
    args = {
        'user': request.user
    }
    return render(request, 'accounts/home.html', args)
