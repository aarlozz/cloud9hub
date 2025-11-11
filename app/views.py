from django.shortcuts import render
from . forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(user,request)
            return redirect ('dashboard')
    else:
            form=UserCreationForm()

    return render(request, 'signupform.html', {'form': form})        

# Create your views here.

