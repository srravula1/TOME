# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-23 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0031_auto_20180523_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletopicrank',
            name='rank',
            field=models.IntegerField(default=-1),
        ),
    ]
