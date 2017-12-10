# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_lecture', '0004_auto_20171210_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_lecturer.Lecturer'),
        ),
    ]
