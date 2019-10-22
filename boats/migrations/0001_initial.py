# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-20 18:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=250, null=True)),
                ('replacement_value', models.CharField(max_length=250, null=True)),
                ('insured', models.BooleanField(default=False)),
                ('insurance_policy', models.CharField(max_length=250, null=True)),
                ('build_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoatImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat_image', models.FileField(upload_to='boats')),
                ('profile_image', models.BooleanField(default=False)),
                ('caption', models.TextField(null=True)),
                ('title', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoatOwners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250, null=True)),
                ('person_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=250)),
                ('build_year', models.DateField()),
                ('make', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngineServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('next_service', models.DateField()),
                ('notes', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HullColours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='engine',
            name='services',
            field=models.ManyToManyField(to='boats.EngineServices'),
        ),
        migrations.AddField(
            model_name='boat',
            name='engine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boats.Engine'),
        ),
        migrations.AddField(
            model_name='boat',
            name='hull_colour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boats.HullColours'),
        ),
        migrations.AddField(
            model_name='boat',
            name='images',
            field=models.ManyToManyField(to='boats.BoatImages'),
        ),
        migrations.AddField(
            model_name='boat',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boats.BoatOwners'),
        ),
    ]