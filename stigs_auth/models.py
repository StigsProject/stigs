from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    # Additional attributes of UserProfile.
    about_me = models.TextField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    # see https://docs.djangoproject.com/en/1.6/ref/models/fields/
    website = models.URLField(blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    flattr = models.CharField(max_length=100, blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        app_label = 'auth'
        db_table = 'auth'

    def __unicode__(self):
        return self.username