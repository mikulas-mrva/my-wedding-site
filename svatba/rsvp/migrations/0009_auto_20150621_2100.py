# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0008_auto_20150621_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 21, 0, 11, 85741), editable=False),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 21, 0, 11, 85794)),
        ),
    ]
