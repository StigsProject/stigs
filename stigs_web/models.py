from django.db import models
from stigs_auth.models import UserProfile


class UserData(models.Model):
    users = models.ManyToManyField(UserProfile)

    class Meta:
        abstract = True


class Stig(UserData):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')

    class Meta:
        app_label = 'stigs_web'
        permissions = (
            ("change_own_stig", "Can change own stig"),
            ("delete_own_stig", "Can delete own stig"),
        )

    def __unicode__(self):
        return self.title

    def creator(self):
        return self.users.first()

    @staticmethod
    def is_owner(obj, user):
        return obj.users.filter(username__exact=user).exists()

    @staticmethod
    def published_last():
        return Stig.objects.order_by('-pub_date')[:5]

