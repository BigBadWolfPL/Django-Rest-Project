from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm): # dodanie maila do UCF. w views.py użyć UserRegisterForm
   email = forms.EmailField() # pola do dodania/a poniżej do edycji.

   class Meta:
      model = User  # Wskazuje model z jakim chcemy pracować.
      fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm): # Edycja nazwy uzytkownika oraz maila.
   email = forms.EmailField()

   class Meta:
      model = User
      fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
   
   class Meta: # tutaj edytujemy profil (zdj profilowe.)
      model = Profile
      fields = ['image']