# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='present',
            name='unlimited',
            field=models.BooleanField(help_text='může si ho vybrat víc lidí a nikdy se neškrtne', default=False, verbose_name='Příspěvek'),
        ),
    ]
