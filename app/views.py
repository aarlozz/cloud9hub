from django.shortcuts import render
from . forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Event
def signup_view(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect ('dashboard')
    else:
            form=UserCreationForm()

    return render(request, 'signupform.html', {'form': form})        


def login_view(request):
    if request.method=='POST': #esko 2 ta methoid hunxa get garda ni hunxa request.POST.get('username') kei data xaina vane nine dinxa
        username=request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print("login successful")
            return redirect('dashboard')
        else:
             print("login failed")
             return render(request, 'signupform.html')
        
    return render(request, 'login.html')  

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
        event = Event.objects.all().order_by('-created_at')
        return render(request, 'dashboard.html',{'events': event}) 

def create_event_view(request):
    if request.method == 'POST':
        title = request.POST.get('event_title')
        description = request.POST.get('description')


        Event.objects.create(
            event_title=title,
            description=description,
        )

        return redirect('dashboard')
    return render(request, 'create_event.html')
