# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('name', models.CharField(max_length=100, verbose_name='Jméno')),
            ],
            options={
                'verbose_name': 'Hosté',
                'ordering': ['email'],
                'verbose_name_plural': 'Host',
            },
        ),
    ]
