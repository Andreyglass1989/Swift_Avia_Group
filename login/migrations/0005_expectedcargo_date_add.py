# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-14 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_expectedcargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='expectedcargo',
            name='date_add',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
