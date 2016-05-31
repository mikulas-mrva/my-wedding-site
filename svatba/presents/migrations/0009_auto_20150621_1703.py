# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0008_auto_20150610_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 17, 3, 9, 288112), editable=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 17, 3, 9, 288181)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 17, 3, 9, 286652), editable=False),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 17, 3, 9, 286725)),
        ),
    ]
