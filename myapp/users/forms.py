from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import users

class LoginForm(forms.Form):
    '''
    A login form prompted to the user for login acess.
    '''
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget = forms.PasswordInput)

    def clean_data(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        return username, password
    
    def check(self, username, password):
        user = users.objects.filter(username=username)
        if user or username=='' or password =='': return False
        return True
    
    def save(self, username, password):
        user = users(username=username)
        user.set_password(password)
        user.save()
        return user

class ProfileForm(forms.Form):
    email    = forms.CharField(label='email')
    name     = forms.CharField(label='name')
    country  = forms.CharField(label='country')
    dob      = forms.DateField(label='dob')

    def change(self, user):
        user.email   = self.cleaned_data['email']
        user.name    = self.cleaned_data['name']
        user.country = self.cleaned_data['country']
        user.dob     = self.cleaned_data['dob']
        try:
            user.save()
            return True
        except:
            return False

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = users
        fields = ('username', 'email', 'name', 'dob', 'country',
        'image')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = users
        fields = ('username', 'email', 'name', 'dob', 'country',
        'image', 'contribution', 'is_admin', 'is_mod', 'is_active', 'is_staff')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('dob', 'name', 'country', 'image', 'contribution', )}),
        ('Permissions', {'fields': ('is_admin', 'is_mod', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()