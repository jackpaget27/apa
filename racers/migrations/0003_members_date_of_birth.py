# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-20 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racers', '0002_auto_20191020_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]