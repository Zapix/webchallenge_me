# -*- coding: utf-8 -*-
import magic

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
    image = models.ImageField(
        upload_to=lambda instance, name: 'job_{}/{}'.format(instance.job_id,
                                                            name)
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created', )

    def __unicode__(self):
        return self.image.name or 'New Image'

    def __repr__(self):
        return '<ImageInfo {}, pk {}>'.format(unicode(self), self.pk)

    @property
    def width(self):
        assert self.pk
        return self.image.width

    @property
    def height(self):
        assert self.pk
        return self.image.height

    @property
    def size(self):
        assert self.pk
        return self.image.size

    @property
    def url(self):
        assert self.pk
        return self.image.url

    @property
    def path(self):
        assert self.pk
        return self.image.path

    @property
    def mimetype(self):
        assert self.pk
        return magic.from_file(self.path, True)
