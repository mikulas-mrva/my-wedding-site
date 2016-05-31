# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0003_auto_20150610_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 13, 24, 49, 367809), editable=False),
        ),
        migrations.AddField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 13, 24, 49, 367863)),
        ),
        migrations.AddField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 13, 24, 49, 366435), editable=False),
        ),
        migrations.AddField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 13, 24, 49, 366505)),
        ),
    ]
