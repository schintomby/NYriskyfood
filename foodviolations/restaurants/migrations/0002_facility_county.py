# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='county',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
