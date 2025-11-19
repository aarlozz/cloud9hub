from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    petname = models.CharField(max_length=30, blank=True, default='user')

    def __str__(self):
        return f"{self.user.username} - {self.petname}"


class Event(models.Model):
    profile = models.ForeignKey(Profile, related_name="events", on_delete=models.CASCADE)

    event_title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)


    rating = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text="Rating from 1 to 10"
    )

    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    highlight = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event_title} - {self.created_by}"


class Task(models.Model):
    profile = models.ForeignKey(Profile, related_name="tasks", on_delete=models.CASCADE)

    task_title = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text="Rating from 1 to 10"
    )

    status = models.CharField(
    max_length=20,
    choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ],
    default='pending'
)


    created_by = models.CharField(max_length=50)
    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    highlight = models.BooleanField(default=False)

    def days_remaining(self):
        from datetime import date
        return (self.deadline - date.today()).days

    def __str__(self):
        return f"{self.task_title} - {self.created_by}"
