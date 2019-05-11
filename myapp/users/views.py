from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, get_user
from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework.generics import ListAPIView
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.permissions import IsAuthenticated

from .forms import ProfileForm, LoginForm
from .backend import getUserdata

class login_view(APIView):
    '''
    Renders login page, If user allredy logged in 
    redirects to main page.
    '''
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main/')
        return render(request, 'accounts/login.html')
    
    '''
    API gives back JSON data,  boolean value
    if user is sucessfully logged in.

    requirement: POST param: page (username, password)

    return JSON format (each field):
    {
        status
    }
    '''
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
    '''
    API gives back JSON data,  boolean value
    if user is sucessfully registered.

    requirement: POST param: page (username, password, repassword)

    return JSON format (each field):
    {
        status
    }
    '''
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
    '''
    Renders profile page with user profile
    data if the user is logged in.
    '''
    def get(self, request):
        user = get_user(request)
        data = getUserdata(user)
        return render(request, 'accounts/profile.html', data)
    
    '''
    API gives back JSON data,  boolean value
    if user is data is successfully updated.

    requirement: POST param: page (email, country, name, dob, image)

    return JSON format (each field):
    {
        status
    }
    '''
    def post(self, request):
        status = False
        image  = request.FILES.get('image', None)
        form = ProfileForm(request.POST)
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

def logout_view(request):
    logout(request)
    return redirect('login')
