# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_remove_users_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
