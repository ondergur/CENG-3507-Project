# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lecture', '0005_auto_20171210_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='aciklama',
            field=models.TextField(default='kisaaciklama'),
            preserve_default=False,
        ),
    ]