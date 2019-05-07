from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, get_user
from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated

from .forms import ProfileForm, LoginForm
from .backend import getUserdata

class login_view(APIView):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        form  = LoginForm(request.POST)
        status = False
        if form.is_valid():
            username, password = form.clean_data()
            user = authenticate(
                username=username,
                password=password
            )
            if user:
                login(request, user)
                status= True
        return Response({
            'success': status
        })

class register_view(APIView):
        
    def get(self):
        pass

    def post(self, request):
        form = LoginForm(request.POST)
        status = False
        if form.is_valid():
            username, password = form.clean_data()
            if form.check(username, password):
                status = True
                user = form.save(username, password)
                login(request, user)
        return Response({
            'success': status
        })

class profile_view(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = get_user(request)
        data = getUserdata(user)
        return render(request, 'accounts/profile.html', data)

    def post(self, request):
        status = False
        image  = request.FILES.get('image', None)
        print(image)
        form = ProfileForm(request.POST)
        print(form.data)
        if form.is_valid():
            print('a valid form')
            user = get_user(request)
            if image: user.image = image
            status = form.change(user)       
        else:
            print('not a valid form')
        return Response({
            'success': status
        })        

@login_required()
def main_view(request):
    args = {
        'user': request.user
    }
    return render(request, 'accounts/main.html', args)

def logout_view(request):
    logout(request)
    return redirect('login')
