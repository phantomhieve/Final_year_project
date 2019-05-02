from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .forms import UserCreationForm
from .models import users


class login_view(APIView):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        # need to clean data here
        username = request.POST.get('username', '')
        password = request.POST.get('pass', '')
        user = authenticate(
            username=username,
            password=password
        )
        status = False
        if user:
            login(request, user)
            status = True
        return Response({
            'success': status
        })

class check_view(APIView):
    def get(self, request):
        pass

    def post(self, request):

        # need to clean data here
        username = request.POST.get('name', '')
        password = request.POST.get('pass', '')
        status = True
        user = users.objects.filter(username=username)
        if user or username=='' or password =='': 
            status = False
        else:
            user = users(username=username)
            user.set_password(password)
            user.save()
            login(request, user)
        return Response({
            'success': status
        })

class register_view(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)

    def post(self, request):
        pass

@login_required()
def main_view(request):
    args = {
        'user': request.user
    }
    return render(request, 'accounts/main.html', args)

def logout_view(request):
    logout(request)
    return redirect('login')
