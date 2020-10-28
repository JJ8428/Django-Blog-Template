from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Every time a user is made, we want the profile class made for each user
@receiver(post_save, sender=User) # How are calling this function? We are using a signal reciever that will detect when a user 
def create_profile(sender, instance, created, **kwargs): # Instance passed in is the User
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): # Instance passed in is the User
    instance.profile.save()

# For me to use these receivers, I need to import them into this app's apps.py
# receiver decorators are constantly listening for that signal to trigger the function 