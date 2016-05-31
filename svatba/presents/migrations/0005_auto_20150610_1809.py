# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0004_auto_20150610_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 10, 18, 9, 42, 145841)),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 18, 9, 42, 145895)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 10, 18, 9, 42, 144422)),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 18, 9, 42, 144492)),
        ),
    ]
