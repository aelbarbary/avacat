# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avacatapp', '0016_auto_20170523_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='created_by_user',
            new_name='created_by',
        ),
    ]
