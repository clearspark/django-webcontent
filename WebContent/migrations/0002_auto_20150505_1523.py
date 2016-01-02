# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebContent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='created',
            field=models.DateField(default='2000-01-01', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='edited',
            field=models.DateField(default='2011-01-01', auto_now=True),
            preserve_default=False,
        ),
    ]
