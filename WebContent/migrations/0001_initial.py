# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=200)),
                ('pub_date', models.DateField(verbose_name=b'Date published')),
            ],
        ),
        migrations.CreateModel(
            name='ContentTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='WebContent.Content')),
                ('fileContent', models.FileField(null=True, upload_to=b'uploads/webcontent/%Y/%m/%d/', blank=True)),
            ],
            bases=('WebContent.content',),
        ),
        migrations.CreateModel(
            name='HyperLink',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='WebContent.Content')),
                ('target', models.URLField()),
            ],
            bases=('WebContent.content',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='WebContent.Content')),
                ('html', models.TextField()),
            ],
            bases=('WebContent.content',),
        ),
        migrations.AddField(
            model_name='content',
            name='authGroup',
            field=models.ManyToManyField(help_text=b'Groups who are allowed to view content', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(to='WebContent.ContentTag'),
        ),
    ]
