# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Credentials',
        ),
    ]
