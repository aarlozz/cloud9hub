from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, timedelta

from .models import Profile, Event, Task


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="anil", password="anil")
        self.profile = Profile.objects.create(user=self.user, petname="acess")

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "anil - acess")


class EventModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="eventanil", password="anil")
        self.profile = Profile.objects.create(user=self.user)
        
        self.event = Event.objects.create(
            profile=self.profile,
            event_title="Ghumna Jani",
            description="A fun trip event",
            rating=5,
            created_by="eventanil"
        )

    def test_event_str(self):
        self.assertEqual(str(self.event), "Ghumna Jani - eventanil")

    def test_event_rating(self):
        self.assertIsInstance(self.event.rating, int)
        self.assertTrue(1 <= self.event.rating <= 10)


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="taskanil", password="anil")
        self.profile = Profile.objects.create(user=self.user)

        self.deadline = date.today() + timedelta(days=5)

        self.task = Task.objects.create(
            profile=self.profile,
            task_title="Select Location",
            rating=8,
            created_by="taskanil",
            deadline=self.deadline
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), "Select Location - taskanil")

    def test_task_days_remaining(self):
        days = self.task.days_remaining()
        self.assertEqual(days, 5)

    def test_task_deadline_type(self):
        self.assertIsInstance(self.task.deadline, date)

    def test_task_rating_limit(self):
        self.assertTrue(1 <= self.task.rating <= 10)
