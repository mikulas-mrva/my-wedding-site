# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0012_auto_20150622_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 21, 6, 2, 149548)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 21, 6, 2, 149608)),
        ),
    ]
