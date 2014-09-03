# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date created')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('change_own_stig', 'Can change own stig'), ('delete_own_stig', 'Can delete own stig')),
            },
            bases=(models.Model,),
        ),
    ]
