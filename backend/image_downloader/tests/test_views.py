# -*- coding: utf-8 -*-
import os

import faker
import mock
from mock import MagicMock

from django.core.files import File
from django.core.files.images import ImageFile
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .. import models


class FakerAPITestCase(APITestCase):

    def setUp(self):
        super(FakerAPITestCase, self).setUp()
        self.faker = faker.Factory.create()


class JobCreateTestCase(FakerAPITestCase):
    tasks_patch = None

    def setUp(self):
        super(JobCreateTestCase, self).setUp()

        self.tasks_patch = mock.patch(
            'image_downloader.signals.tasks',
            MagicMock(),
        )
        self.tasks_patch.start()

    def tearDown(self):
        super(JobCreateTestCase, self).tearDown()
        self.tasks_patch.stop()

    def create_job(self):
        return models.Job.objects.create(
            url=self.faker.url(),
            state=models.JobStateChoices.finished
        )


class ImageCreateTestCase(APITestCase):

    def create_image_info(self, job):
        image_info = models.ImageInfo()
        image_info.job = job

        file_path = os.path.join(
            os.path.dirname(__file__),
            'data/googlelogo_color_272x92dp.png'
        )
        data_file = ImageFile(
            File(open(file_path, 'rb'))
        )
        image_info.image.save(
            os.path.basename(file_path),
            data_file
        )
        image_info.save()
        return image_info


class JobAPITestCase(JobCreateTestCase):

    def test_get_job_list(self):
        response = self.client.get(
            reverse(
                'job-list',
            )
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_job(self):
        response = self.client.post(
            reverse(
                'job-list'
            ),
            {
                'url': self.faker.url()
            }
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_job_success(self):
        job = self.create_job()

        response = self.client.get(
            reverse(
                'job-detail',
                kwargs={
                    'pk': job.pk
                }
            )
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )


class ImageAPITestCase(JobCreateTestCase, ImageCreateTestCase):

    def test_get_image_list_for_job_success(self):
        job = self.create_job()

        response = self.client.get(
            reverse(
                'image-list',
                kwargs={
                    'job_pk': job.pk
                }
            )
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_image_list_for_job_not_found(self):
        response = self.client.get(
            reverse(
                'image-list',
                kwargs={
                    'job_pk': 323
                }
            )
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_get_image(self):
        job = self.create_job()
        image_info = self.create_image_info(job)

        response = self.client.get(
            reverse(
                'image-detail',
                kwargs={
                    'job_pk': job.pk,
                    'pk': image_info.pk
                }
            )
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
