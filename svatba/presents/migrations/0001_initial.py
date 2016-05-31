# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('email', models.EmailField(verbose_name='email', max_length=254)),
                ('removed', models.BooleanField(verbose_name='zruseno', default=False)),
            ],
            options={
                'verbose_name_plural': 'Dárci',
                'verbose_name': 'Dárce',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(verbose_name='Název', max_length=30)),
                ('link', models.CharField(blank=True, null=True, verbose_name='Odkaz', max_length=300)),
                ('description', models.TextField(null=True, verbose_name='Popis', blank=True)),
                ('price', models.IntegerField(null=True, verbose_name='Přibližná cena')),
                ('priority', models.PositiveSmallIntegerField(verbose_name='Priorita')),
            ],
            options={
                'verbose_name_plural': 'Dary',
                'verbose_name': 'Dar',
                'ordering': ['priority'],
            },
        ),
        migrations.AddField(
            model_name='person',
            name='present',
            field=models.ForeignKey(to='presents.Present', verbose_name='dar'),
        ),
    ]
