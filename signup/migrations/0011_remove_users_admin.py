# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0010_remove_users_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='admin',
        ),
    ]
