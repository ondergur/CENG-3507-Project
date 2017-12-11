# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_lecture', '0003_lecture_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecturer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app_lecturer.Lecturer'),
        ),
    ]