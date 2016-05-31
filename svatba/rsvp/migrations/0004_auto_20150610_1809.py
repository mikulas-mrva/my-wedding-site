# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_auto_20150610_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 10, 18, 9, 42, 147888)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 18, 9, 42, 147958)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='note',
            field=models.TextField(verbose_name='Poznámka', null=True, help_text='Prosíme o upřesnění dalších případných stravovacích omezení či menšinových návyků.', max_length=500),
        ),
    ]
