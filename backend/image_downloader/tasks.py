# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from celery import chord

from . import models
from . import utils


@shared_task
def download_image_from_url(job_pk, url):
    data = utils.get_image_by_url(url)
    if data is None:
        return
    image, filename = data

    image_info = models.ImageInfo()
    image_info.job_id = job_pk
    image_info.image.upload_to = 'job_{}'.format(job_pk)
    image_info.image.save(
        filename,
        image
    )
    image_info.save()


@shared_task
def finish_downloading(result, job_pk):
    job = models.Job.objects.get(pk=job_pk)
    job.state = models.JobStateChoices.finished
    job.save()


@shared_task
def download_image(job_pk):
    job = models.Job.objects.get(pk=job_pk)
    job.state = models.JobStateChoices.running
    job.save()

    urls = utils.get_image_links_from_url(job.url)

    chord(
        (download_image_from_url.s(job_pk, url) for url in urls),
        finish_downloading.s(job_pk)
    ).apply_async()
