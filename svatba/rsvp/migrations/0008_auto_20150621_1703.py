# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0007_auto_20150610_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='attending',
            field=models.BooleanField(default=True, verbose_name='Přijdu'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='baker',
            field=models.BooleanField(default=False, verbose_name='Rád/a pomůžu s vařením nebo pečením na hostinu'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 17, 3, 9, 290271), editable=False),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 17, 3, 9, 290324)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='note',
            field=models.TextField(help_text='Prosíme o upřesnění dalších případných stravovacích omezení.', max_length=500, verbose_name='Poznámka', null=True),
        ),
    ]
