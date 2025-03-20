# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebContent', '0006_contenttag_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(on_delete=models.CASCADE, to='auth.User'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=models.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebContent.Content'),
        ),
        migrations.AlterField(
            model_name='hyperlink',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=models.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebContent.Content'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=models.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebContent.Content'),
        ),
    ] 