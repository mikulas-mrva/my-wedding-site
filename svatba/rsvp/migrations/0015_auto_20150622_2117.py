# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0014_auto_20150622_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='note',
        ),
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 21, 17, 37, 11774), editable=False),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 21, 17, 37, 11828)),
        ),
    ]
