from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#this says that the SignupForm is inheroted from the UserCreationForm
class SignupForm(UserCreationForm):
    name=forms.CharField(required=True)
    email= forms.EmailField(required=True)

    class Meta:
        model=User # This tells that the model is linked with inbuilt User model
        fields=['username','email', 'password1','password2']

#form ma widget use garera forntend use garney

