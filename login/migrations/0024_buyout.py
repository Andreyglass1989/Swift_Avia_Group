# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-11-14 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0006_auto_20171104_1755'),
        ('login', '0023_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('size', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('1', '\u041e\u043f\u043b\u0430\u0447\u0435\u043d'), ('2', '\u0412\u044b\u043a\u0443\u043f\u043b\u0435\u043d\u043e'), ('3', '\u041e\u0436\u0438\u0434\u0430\u0435\u0442\u044c\u0441\u044f \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435'), ('4', '\u0414\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u043d\u0430 \u0441\u043a\u043b\u0430\u0434'), ('5', '\u041b\u0435\u0442\u0438\u0442 \u0432 \u0423\u043a\u0440\u0430\u0438\u043d\u0443'), ('6', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u043a\u043b\u0438\u0435\u043d\u0442\u0443')], max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.Customer')),
            ],
        ),
    ]
