from django.contrib import admin
from . models import Profile, Event, Task


# Register your models here.
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Task)
