# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20150610_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='baker',
            field=models.BooleanField(verbose_name='Rád/a pomůžu s pečením', default=False),
        ),
        migrations.AddField(
            model_name='visitor',
            name='gluten_free',
            field=models.BooleanField(verbose_name='Nemůžu lepek', default=False),
        ),
        migrations.AddField(
            model_name='visitor',
            name='note',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='vegan',
            field=models.BooleanField(verbose_name='Jsem vegan', default=False),
        ),
        migrations.AddField(
            model_name='visitor',
            name='vegetarian',
            field=models.BooleanField(verbose_name='Jsem vegetarian', default=False),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 17, 52, 50, 405350), editable=False),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 17, 52, 50, 405401)),
        ),
    ]
