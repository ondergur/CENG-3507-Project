# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-28 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lecture', '0008_auto_20171228_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='secme',
            field=models.CharField(blank=True, choices=[('Seçmeli', 'Seçmeli'), ('Zorunlu', 'Zorunlu')], max_length=20, null=True),
        ),
    ]
