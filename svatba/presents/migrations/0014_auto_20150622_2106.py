# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0013_auto_20150622_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='present',
            name='plural',
            field=models.BooleanField(verbose_name='plurál', default=False, help_text='nech nezaskrtnuto pro singular'),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 21, 6, 2, 147324)),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 21, 6, 2, 147395)),
        ),
        migrations.AlterField(
            model_name='present',
            name='created_at',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 22, 21, 6, 2, 145677, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='present',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 22, 21, 6, 2, 145759, tzinfo=utc)),
        ),
    ]
