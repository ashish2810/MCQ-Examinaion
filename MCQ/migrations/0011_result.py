# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0010_auto_20170215_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCQ.Exam')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCQ.Student')),
            ],
        ),
    ]