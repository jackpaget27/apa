# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-20 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoponsorshipLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('value', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorBenefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('value', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorContracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('file_contract', models.FileField(upload_to='media/sponsors/contracts')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media/sponsors/logos')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=250)),
                ('sponsor_nation', django_countries.fields.CountryField(max_length=2)),
                ('facebook_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('insta_handle', models.CharField(blank=True, max_length=250, null=True)),
                ('company_site', models.CharField(blank=True, max_length=250, null=True)),
                ('profile_text', models.TextField(blank=True, null=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('telephone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('address_line_1', models.CharField(max_length=250)),
                ('address_line_2', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line_3', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line_4', models.CharField(blank=True, max_length=250, null=True)),
                ('address_country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('sign_up_date', models.DateField(auto_now_add=True)),
                ('active_sponsor', models.BooleanField(default=True)),
                ('driver_sponsor', models.BooleanField(default=False)),
                ('contract', models.ManyToManyField(to='sponsors.SponsorContracts')),
                ('driver_sponsored', models.ManyToManyField(to='drivers.Driver')),
                ('logo', models.ManyToManyField(to='sponsors.SponsorLogo')),
                ('payments', models.ManyToManyField(to='sponsors.SponsorPayments')),
            ],
        ),
        migrations.AddField(
            model_name='soponsorshiplevel',
            name='benefits',
            field=models.ManyToManyField(to='sponsors.SponsorBenefits'),
        ),
    ]