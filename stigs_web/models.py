from django.db import models


class Stig(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    @staticmethod
    def published_last():
        return Stig.objects.order_by('-pub_date')[:5]