# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avacatapp', '0010_auto_20170522_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='likes',
        ),
    ]