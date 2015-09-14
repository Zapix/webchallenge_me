# -*- coding: utf-8 -*-
from django.apps.config import AppConfig


class ImageDownloaderAppConfig(AppConfig):
    name = 'image_downloader'
    verbose_name = 'Image downloader'

    def ready(self):
        from . import signals  # flake8: noqa

