# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-20 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_auto_20181126_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/Buyout'),
        ),
    ]
