# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=200)),
                ('exam', models.IntegerField()),
                ('version', models.IntegerField()),
                ('discipline', models.IntegerField()),
            ],
        ),
    ]
