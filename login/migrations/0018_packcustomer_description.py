# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-07 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_packcustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='packcustomer',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
