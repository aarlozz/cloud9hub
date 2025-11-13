from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.home_view, name='dashboard'),
    path('create_event/', views.create_event_view, name='create_event'), 
    ]

