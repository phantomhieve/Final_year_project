from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import LoginForm, UserChangeForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserCreationForm()
    args = {'form': form}
    return render(request, 'accounts/register.html', args)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email, password = form.clean_data()
            user = authenticate(
                email = email, 
                password = password
            )
            if user:
                login(request, user)
                return redirect(main_view)
        return redirect(login_view)
    form = LoginForm()
    args = {'form': form}
    return render(request, 'accounts/login.html', args)

@login_required
def main_view(request):
    print('Here')
    args = {
        'user': request.user
    }
    return render(request, 'accounts/main.html', args)