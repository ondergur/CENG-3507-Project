# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-16 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lecturer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
