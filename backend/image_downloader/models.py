# -*- coding: utf-8 -*-
from django.db import models

from djchoices import DjangoChoices, ChoiceItem


class JobStateChoices(DjangoChoices):

    not_started = ChoiceItem('not_started', 'Not Started')
    running = ChoiceItem('running', 'Running')
    failed = ChoiceItem('failed', 'Failed')
    finished = ChoiceItem('finished', 'Finished')


class Job(models.Model):
    url = models.URLField()
    state = models.CharField(
        max_length=255,
        choices=JobStateChoices.choices,
        default=JobStateChoices.not_started
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ('-created', )

    def __unicode__(self):
        if self.pk:
            return u'Job for: {}'.format(self.url)
        return 'New Job'

    def __repr__(self):
        return '<{}, pk: {}>'.format(
            unicode(self),
            self.pk
        )


class ImageInfo(models.Model):
    job = models.ForeignKey(
        'Job',
        related_name='images'
    )
    name = models.CharField(
        'Image name',
        max_length=255
    )
    original_url = models.URLField()
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    size_in_bytes = models.PositiveIntegerField()
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created', )

    def __unicode__(self):
        return self.name or 'New Image'

    def __repr__(self):
        return '<ImageInfo {}, pk {}>'.format(unicode(self), self.pk)
