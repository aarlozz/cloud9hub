from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Event, Task


class SignupForm(UserCreationForm):
    name = forms.CharField(
        required=True,
        label="Full Name",
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
            'placeholder': 'Enter your full name'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
            'placeholder': 'Choose a username'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
            'placeholder': 'Enter password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# -------------------------
# Profile Form
# -------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['petname']  # Only include existing fields

        widgets = {
            'petname': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'placeholder': 'Enter your petname'
            }),
        }



# -------------------------
# Event Form
# -------------------------
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_title', 'description', 'rating', 'date']

        widgets = {
            'event_title': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'placeholder': 'Enter event title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'placeholder': 'Enter event description',
                'rows': 4
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'placeholder': 'Rating out of 5'
            }),
            'date': forms.DateInput(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'type': 'date'
            }),
        }


# -------------------------
# Task Form
# -------------------------
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'rating', 'deadline']

        widgets = {
            'task_title': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'placeholder': 'Enter task title'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'placeholder': 'Rating out of 5'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'w-full border rounded-lg p-3 focus:ring-2 focus:ring-orange-400',
                'type': 'date'
            }),
        }