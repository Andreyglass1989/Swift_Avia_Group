# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-01-04 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Izrael', '0002_auto_20190104_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='izraeldataforpacking',
            name='date_add',
            field=models.DateTimeField(auto_now=True),
        ),
    ]