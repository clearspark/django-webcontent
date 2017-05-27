# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebContent', '0002_auto_20150505_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='authGroup',
            field=models.ManyToManyField(help_text='Groups who are allowed to view content', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateField(verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='fileContent',
            field=models.FileField(upload_to='uploads/webcontent/%Y/%m/%d/'),
        ),
    ]
