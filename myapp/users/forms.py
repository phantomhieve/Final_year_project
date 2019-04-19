from django.forms import ModelForm
from django import forms
from .models import users, special

class RegistrationForm(forms.Form):

    DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015')

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
            image    = self.getHash(profile),
            name     = name,
            username = username,
            email    = email,
            password = self.encrypt(password),
            country  = country,
            dob      = dob
        )
        try:
            ob.save()
        except:
            return False
        return True
    
    def getHash(self, image):
        return '1234'
    
    def encrypt(self, password):
        return password

