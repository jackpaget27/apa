# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-21 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racers', '0004_racinglicensescans_license_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identityscans',
            name='file',
            field=models.FileField(upload_to='identity'),
        ),
        migrations.AlterField(
            model_name='racinglicensescans',
            name='file',
            field=models.FileField(upload_to='licenses'),
        ),
    ]