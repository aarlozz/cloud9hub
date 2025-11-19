from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # login/logout first
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),

    # landing page
    path('', views.landing_page, name='landing'),

    # dashboard and signup
    path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),

    # Profile
    path("profile/<int:pk>/", views.profile_detail, name="profile-detail"),

    # Events
    path("events/", views.event_list, name="event-list"),
    path("events/create/", views.event_create, name="event-create"),
    path("events/<int:pk>/", views.event_detail, name="event-detail"),
    path("events/<int:pk>/update/", views.event_update, name="event-update"),
    path("events/<int:pk>/delete/", views.event_delete, name="event-delete"),

    # Tasks
    path("tasks/", views.task_list, name="task-list"),
    path("tasks/create/", views.task_create, name="task-create"),
    path("tasks/<int:pk>/", views.task_detail, name="task-detail"),
    path("tasks/<int:pk>/update/", views.task_update, name="task-update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task-delete"),
]
