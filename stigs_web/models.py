from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    users = models.ManyToManyField(User)

    class Meta:
        abstract = True


class Stig(UserData):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    @staticmethod
    def published_last():
        return Stig.objects.order_by('-pub_date')[:5]

    @staticmethod
    def creator():
        return Stig.objects.get(pk=1).users.first()