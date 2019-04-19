from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('working')
            form.save()
    form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/register.html', args)
