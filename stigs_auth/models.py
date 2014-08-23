from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    about_me = models.TextField(blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=100, blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        app_label = 'auth'