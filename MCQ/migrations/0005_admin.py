# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0004_auto_20170210_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('credentials', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCQ.Credentials')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
