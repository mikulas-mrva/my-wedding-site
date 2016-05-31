# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0009_auto_20150621_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='present',
            name='genus',
            field=models.PositiveSmallIntegerField(choices=[(10, 'mužský'), (20, 'ženský'), (30, 'střední')], default=10, verbose_name='rod'),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 21, 0, 11, 83481), editable=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 21, 0, 11, 83537)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 21, 0, 11, 81550), editable=False),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 21, 0, 11, 81627)),
        ),
    ]
