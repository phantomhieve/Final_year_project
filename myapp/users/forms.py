from django.forms import ModelForm
from django import forms
from .models import users, special

class RegistrationForm(ModelForm):
    class Meta:
        model = users
        fields = (
            'username',
            'name',
            'country',
            'email'
        )
    profile = forms.ImageField(required = False)
    
    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.username = self.cleaned_data['username']
        user.name = self.cleaned_data['name']
        user.country = self.cleaned_data['country']
        user.email = self.cleaned_data['email']
        '''Date input format not working'''
        user.dob = '2012-12-12'
        #user.dob = self.cleaden_data['dob']
        # modify for profile here store hash in 
        user.image = '1234'
        # -------------------------------------
        if commit: 
            sp = special(userna = user.pk)
            print(user.id)
            print(sp.id)
            user.special = sp.pk
            sp.save()
            user.save()
        return user

