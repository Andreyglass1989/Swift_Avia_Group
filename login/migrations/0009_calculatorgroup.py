# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-15 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_file_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
    ]
