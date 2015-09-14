# -*- coding: utf-8 -*-
from django import dispatch
from django.db.models import signals


from . import models
from . import tasks


@dispatch.receiver(signals.post_save, sender=models.Job)
def create_celery_task_for_new_job(sender, instance, created, **kwargs):

    if created:
        tasks.download_image.delay(instance.pk)
