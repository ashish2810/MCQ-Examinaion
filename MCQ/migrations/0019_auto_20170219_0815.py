# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0018_auto_20170219_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='answer_key',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCQ.AnswerKey'),
        ),
    ]