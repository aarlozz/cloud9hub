from django.shortcuts import render
from . forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . models import Event

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


def login_view(request):
    if request.method=='POST': #esko 2 ta methoid hunxa get garda ni hunxa request.POST.get('username') kei data xaina vane nine dinxa
        username=request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
             return render(request, 'signupform.html')
        
    return render(request, 'login.html')   

@login_required
def dashboard_view(request):
     
    profile= request.user.profile

    if request.method=="POST":
        event_title= request.POST.get('event_title')
        rating= request.POST.get('rating')
        created_by= request.POST.get('created_by')
        description= request.POST.get('description')

        Event.objects.create(profile=profile, event_title=event_title, rating=rating, created_by=created_by, description=description)
    event=Event.objects.filter()

    return render(request, 'dashboard.html', {'profile':profile, 'event':event})    