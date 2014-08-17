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

    class Meta:
        permissions = (
            ("manage_object", "Can manage objects"),
        )

    def __unicode__(self):
        return self.title

    def creator(self):
        return self.users.first()

    @staticmethod
    def published_last():
        return Stig.objects.order_by('-pub_date')[:5]

