# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-28 07:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0006_auto_20171104_1755'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0026_buyout_image'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='ManagerCustomerProfile',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.Customer')),
        #         ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
        #     ],
        # ),
        # migrations.AddField(
        #     model_name='buyout',
        #     name='amount_shipping',
        #     field=models.FloatField(blank=True, null=True),
        # ),
    ]
