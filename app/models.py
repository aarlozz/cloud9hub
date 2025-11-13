from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    petname= models.CharField(max_length=10, blank=True, null='False', default='user')

    def __str__(self):
        return f"{self.user.username}- {self.petname}"
    
class Event(models.Model):
    profile= models.ForeignKey(Profile, related_name="event", on_delete=models.CASCADE,default=1)
    event_title= models.CharField(max_length=25,  default="title", blank='False')
    rating=models.IntegerField(max_length=10, blank=True, null=True) 
    #for rating we can also use PositiveSmallIntegerField
    created_by= models.CharField(max_length=25,  default="user", blank='False')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    description=models.TextField() 
    #esma highlight baki xa

    
    def __str__(self):
        return f'{self.event_title} -{self.created_by}' 
    

class Task(models.Model):
    profile=models.ForeignKey(Profile, related_name="task", on_delete=models.CASCADE)
    task_title= models.CharField(max_length=25,  default="title", blank='False')
    rating=models.IntegerField(max_length=10, blank=True, null=True) 
    #for rating we can also use PositiveSmallIntegerField
    created_by= models.CharField(max_length=25, default="user", blank='False')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deadline=models.DateField()
    #esma deadline bata kati din baki xa vanera milaunnu parxa
    #esma tasks schedule ra highligh baki xa
    
    def __str__(self):
        return f"{self.task_title}-{self.created_by}"
