# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-02 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_file_document_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_document',
            name='name',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterModelTable(
            name='file_document',
            table=None,
        ),
    ]
