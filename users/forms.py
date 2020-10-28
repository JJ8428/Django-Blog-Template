'''
    This file is manually made. This is what we do to make custom forms.
    This is a custom from specifically for registration. We used form 
    provided by django for login. Logout does not need a form.
'''
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 

# We need to create side-class for the FORM to display on the page

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: # Meta tells the order in which the parameter should be asked
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # I don't fully understand but this is a guess
        # django has a list of expected formats and this is one of the many out there, no need to learn other format as this is the only model needed

# For user to update their info, they will need a new form
class UserUpdateForm(forms.ModelForm): # Only update username and email
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']