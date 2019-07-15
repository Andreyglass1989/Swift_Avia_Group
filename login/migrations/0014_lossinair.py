# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-04 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0006_auto_20171104_1755'),
        ('login', '0013_auto_20180302_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='LossInAir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_loss', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price_our', models.FloatField(blank=True, null=True)),
                ('price_client', models.FloatField(blank=True, null=True)),
                ('comment', models.CharField(max_length=150)),
                ('date_shortages', models.DateTimeField(auto_now_add=True)),
                ('air', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.Air')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.Customer')),
                ('name_tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.PackProduct')),
                ('plomba_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.PlombaDimension')),
            ],
        ),
    ]
