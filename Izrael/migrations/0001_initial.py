# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-01-04 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IzraelDataForPacking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_number', models.IntegerField()),
                ('full_customer_name', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=100)),
                ('oblast', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('post_number', models.IntegerField()),
                ('street_home', models.CharField(max_length=255)),
                ('height', models.FloatField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
