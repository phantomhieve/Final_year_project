from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, get_user
from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated

from .forms import UserCreationForm, LoginForm

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

        fname, lname, name  = '', '', user.name
        if name: 
            if ' ' in name:
                index = name.index(' ')
                fname = name[:index+1]
                lname = name[index+1:]
            else:
                fname = name
        data = {
            'username': user.username,
            'email'   : user.email if user.email else '',
            'dob'     : user.dob if user.dob else '',
            'country' : user.country if user.country else '',
            'image'   : user.image,
            'fname'   : fname,
            'lname'   : lname,
        }
        return render(request, 'accounts/profile.html', data)
    def post(self, request):
        print(request.POST)
        status = False
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = get_user(request)
            print(request.POST.get('image', None))
            user.image = request.POST.get('image', None)
            print('Valid form')
            status = form.change(user)
        else:
            print('Not a valid form')
        print(status)        
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
