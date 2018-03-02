# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataFramework',
            fields=[
                ('data_id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('data_title', models.CharField(max_length=200)),
                ('data_tags', models.CharField(max_length=200)),
                ('data_price', models.CharField(max_length=200)),
                ('data_type', models.CharField(max_length=200)),
                ('data_uploader', models.CharField(max_length=200)),
                ('data_category', models.CharField(max_length=200)),
                ('data_path', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]