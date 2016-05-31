# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0005_auto_20150610_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 18, 15, 57, 18958), editable=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 18, 15, 57, 19010)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 18, 15, 57, 17485), editable=False),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 18, 15, 57, 17556)),
        ),
    ]
