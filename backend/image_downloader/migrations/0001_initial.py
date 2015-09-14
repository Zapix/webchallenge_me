# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Image name')),
                ('original_url', models.URLField()),
                ('height', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('size_in_bytes', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('state', models.CharField(default=b'not_started', max_length=255, choices=[(b'not_started', b'Not Started'), (b'running', b'Running'), (b'failed', b'Failed'), (b'finished', b'Finished')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='imageinfo',
            name='job',
            field=models.ForeignKey(related_name='images', to='image_downloader.Job'),
        ),
    ]
