# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_tweet_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('send_from', models.ForeignKey(related_name='send_from', to=settings.AUTH_USER_MODEL)),
                ('send_to', models.ForeignKey(related_name='send_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
