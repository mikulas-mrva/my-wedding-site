# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presents', '0002_auto_20150609_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='present',
            name='link',
            field=models.CharField(verbose_name='Odkaz', null=True, max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='present',
            name='name',
            field=models.CharField(verbose_name='Název', max_length=300),
        ),
        migrations.AlterField(
            model_name='present',
            name='price',
            field=models.IntegerField(verbose_name='Přibližná cena', null=True, blank=True),
        ),
    ]
