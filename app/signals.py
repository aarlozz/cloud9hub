from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile


@receiver(post_save, sender=User)
def update_or_create_profile(instance, sender, created, **kwargs):
    """
    Signal to automatically create or update the Profile
    whenever a User is created or saved.
    """
#esma if the profile xain vane Profile ko obejct banaune xain vane user=John
    # pahile nai xa vane get garney
    profile, _ = Profile.objects.get_or_create(user=instance)

    if created:
        #esma default value haru rakhney 
        pass
#aani aaba vaneko profile save gareny
    profile.save()