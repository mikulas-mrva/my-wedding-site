# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0012_auto_20150622_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='present',
            name='always_taken',
            field=models.BooleanField(verbose_name='Vždy obsazen', default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 20, 51, 31, 459675)),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 20, 51, 31, 459738)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 20, 51, 31, 455528, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 20, 51, 31, 455605, tzinfo=utc)),
        ),
    ]
