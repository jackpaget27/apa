# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-20 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
        ('sponsors', '0001_initial'),
        ('boats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DriverEventPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('drivers', models.ManyToManyField(to='drivers.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='EventHosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('telephone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('address_line_1', models.CharField(max_length=250)),
                ('address_line_2', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line_3', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line_4', models.CharField(blank=True, max_length=250, null=True)),
                ('address_country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('hosting_cost', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('telephone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('address_line_1', models.CharField(max_length=250)),
                ('address_line_2', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line_3', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line_4', models.CharField(blank=True, max_length=250, null=True)),
                ('address_country', django_countries.fields.CountryField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RaceDrivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boats.Boat')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heat', models.CharField(max_length=250)),
                ('race_date_time', models.DateTimeField(null=True)),
                ('event_competitors', models.ManyToManyField(to='events.RaceDrivers')),
                ('event_result', models.ManyToManyField(to='events.Lap')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierContracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.FileField(upload_to='media/supplier/contracts')),
                ('contract_value', models.CharField(max_length=250)),
                ('contract_paid', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SupplierTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='lap',
            name='competitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.RaceDrivers'),
        ),
        migrations.AddField(
            model_name='eventsupplier',
            name='supplier_class',
            field=models.ManyToManyField(to='events.SupplierTypes'),
        ),
        migrations.AddField(
            model_name='eventsupplier',
            name='supplier_contracts',
            field=models.ManyToManyField(to='events.SupplierContracts'),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ManyToManyField(to='events.EventHosts'),
        ),
        migrations.AddField(
            model_name='event',
            name='races',
            field=models.ManyToManyField(to='events.Races'),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(to='sponsors.Sponsors'),
        ),
        migrations.AddField(
            model_name='event',
            name='supplier_contracts',
            field=models.ManyToManyField(to='events.SupplierContracts'),
        ),
        migrations.AddField(
            model_name='drivereventpoints',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='championship',
            name='events',
            field=models.ManyToManyField(to='events.Event'),
        ),
    ]
