# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-07 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebContent', '0004_auto_20200407_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(blank=True, to='WebContent.ContentTag'),
        ),
    ]
