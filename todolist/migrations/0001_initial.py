# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wrk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrk_lst', models.CharField(max_length=100)),
            ],
        ),
    ]
