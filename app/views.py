from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SignupForm, EventForm, TaskForm
from .models import Profile, Event, Task



# Landing Page (public)
def landing_page(request):
    return render(request, 'base.html')  # Render your landing page



# -----------------------
# User Signup
# -----------------------
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Dashboard/Home (after login)
@login_required
def home(request):
    profile = get_object_or_404(Profile, user=request.user)
    events = Event.objects.filter(profile=profile)[:4]
    tasks = Task.objects.filter(profile=profile)[:4]
    return render(request, 'home.html', {'events': events, 'tasks': tasks})


# -----------------------
# Profile Views
# -----------------------
@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    events = profile.events.all() if hasattr(profile, 'events') else []
    tasks = profile.tasks.all()
    return render(request, 'profile_detail.html', {
        'profile': profile,
        'events': events,
        'tasks': tasks
    })


@login_required
def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile_form.html', {'form': form})


# -----------------------
# Event Views
# -----------------------
@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})


@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})


@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event-list')
    return render(request, 'event_confirm_delete.html', {'event': event})


# -----------------------
# Task Views
# -----------------------
@login_required
def task_list(request):
    # Only show tasks for the logged-in user's profile
    tasks = Task.objects.filter(profile__user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # Assign the task to the logged-in user's profile
            task.profile = get_object_or_404(Profile, user=request.user)
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


@login_required
def task_detail(request, pk):
    # Ensure the task belongs to the logged-in user
    task = get_object_or_404(Task, pk=pk, profile__user=request.user)
    return render(request, 'task_detail.html', {'task': task})


@login_required
def task_update(request, pk):
    # Ensure the task belongs to the logged-in user
    task = get_object_or_404(Task, pk=pk, profile__user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})


@login_required
def task_delete(request, pk):
    # Ensure the task belongs to the logged-in user
    task = get_object_or_404(Task, pk=pk, profile__user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'task_confirm_delete.html', {'task': task})
