# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0010_auto_20150621_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 18, 32, 14, 890168), editable=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 18, 32, 14, 890237)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 18, 32, 14, 888628, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 18, 32, 14, 888708, tzinfo=utc)),
        ),
    ]
