from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# creading a user form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_no = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'password1', 'password2']

# updating the form by the user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_no = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username']


# updating the user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

