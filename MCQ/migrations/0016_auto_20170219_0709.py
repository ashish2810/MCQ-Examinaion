# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0015_exam_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credentials',
            options={'verbose_name': 'Credential', 'verbose_name_plural': 'Credentials'},
        ),
    ]
