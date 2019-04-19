from django.forms import ModelForm
from django import forms
from .models import users, special
from .hashutil import makeHash, checkHash

class RegistrationForm(forms.Form):

    DOY = ( i for i in range(1980, 2015) )

    ''' Input fields for the form modify label if required'''
    profile    = forms.ImageField(label='Profile Picture',required = False)
    username   = forms.CharField(label='User Name')
    name       = forms.CharField(label='Name')
    email      = forms.EmailField(label='E-Mail')
    password   = forms.CharField(label='Password', widget = forms.PasswordInput)
    repassword = forms.CharField(label='Re-enter Password', widget = forms.PasswordInput)
    country    = forms.ChoiceField(label='Country', choices = [('india', 'india')])
    dob        = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years = DOY))

    def save(self):

        ''' Cleaning the data '''
        profile   = self.cleaned_data['profile']
        username  = self.cleaned_data['username']
        name      = self.cleaned_data['name']
        email     = self.cleaned_data['email']
        password  = self.cleaned_data['password']
        country   = self.cleaned_data['country']
        dob       = self.cleaned_data['dob']
        
        ob = users(
            image    = profile,
            name     = name,
            username = username,
            email    = email,
            password = makeHash(password),
            country  = country,
            dob      = dob
        )
        try:
            ob.save()
        except:
            return False
        return True


