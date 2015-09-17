# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_downloader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageinfo',
            name='height',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='original_url',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='size_in_bytes',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='width',
        ),
        migrations.AddField(
            model_name='imageinfo',
            name='image',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
