# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170307_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='next_paper',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='news.Newspaper'),
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='prev_paper',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='news.Newspaper'),
        ),
    ]
