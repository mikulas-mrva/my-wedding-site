# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0011_auto_20150622_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 20, 51, 31, 466016)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 20, 51, 31, 466078)),
        ),
    ]
