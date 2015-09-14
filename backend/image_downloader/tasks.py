# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import shared_task

from . import models


@shared_task
def download_image(job_pk):
    job = models.Job.objects.get(pk=job_pk)
    job.state = models.JobStateChoices.running
    job.save()
