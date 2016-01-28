# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
