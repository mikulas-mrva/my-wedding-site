# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0014_auto_20150622_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 21, 16, 31, 618620)),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 21, 16, 31, 618698)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 21, 16, 31, 616621, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 21, 16, 31, 616715, tzinfo=utc)),
        ),
    ]
