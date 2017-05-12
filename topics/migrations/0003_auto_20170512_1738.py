# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20170308_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletopicrank',
            options={'ordering': ('score',)},
        ),
        migrations.AlterModelOptions(
            name='wordtopicrank',
            options={'ordering': ('score',)},
        ),
        migrations.RenameField(
            model_name='articletopicrank',
            old_name='rank',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='wordtopicrank',
            old_name='rank',
            new_name='score',
        ),
    ]
