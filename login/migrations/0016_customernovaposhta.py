# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-04 15:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0006_auto_20171104_1755'),
        ('login', '0015_auto_20180304_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerNovaPoshta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('address_client', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10)])),
                ('comment', models.CharField(blank=True, max_length=150, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.Customer')),
            ],
        ),
    ]
