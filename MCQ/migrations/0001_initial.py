# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.IntegerField(default=0)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
    ]
