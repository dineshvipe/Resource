# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20171113_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
