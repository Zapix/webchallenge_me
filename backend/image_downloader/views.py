# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers


class JobViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    Job resource.
    """
    serializer_class = serializers.JobSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return models.Job.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Creates Job. Gets url for downloading from request and creates a task
        to download images.
        ---
        parameters:
        - name: url
          required: true
          paramType: form
          description: Url from where images will be downloaded
          type: url
        responseMessages:
        - code: 201
          message: Job created
        - code: 400
          message: Error in sent data
        """
        return super(JobViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Return list of jobs and info has we another page with jobs or not.
        ---
        parameters:
        - name: page
          required: false
          paramType: query
          description: Current page number
          type: integer
          format: int32
        """
        return super(JobViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Job detail.
        ---
        parameters:
        - name: pk
          paramType: path
          required: true
          description: Job primary key
        responseMessages:
        - code: 200
          message: Job found
        - code: 404
          message: Job not found
        """
        return super(JobViewSet, self).retrieve(request, *args, **kwargs)


class ImageInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Image resource
    """
    serializer_class = serializers.ImageInfoSerializer
    pagination_class = PageNumberPagination

    def get_job(self):
        return get_object_or_404(
            models.Job,
            pk=self.kwargs['job_pk']
        )

    def get_queryset(self):
        return self.get_job().images.all()

    def list(self, request, *args, **kwargs):
        """
        Get list of images for job and info has we another page or not.
        ---
        parameters:
        - name: job_pk
          paramType: path
          type: integer
          format: int32
          description: Job primary key
        - name: page
          required: false
          paramType: query
          description: Current page number
          type: integer
          format: int32
        responseMessages:
          - code: 200
            message: Everything is Ok. List of images returned
          - code: 404
            message: Job not found
        """
        return super(ImageInfoViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Get detail about image.
        ---
        parameters:
        - name: job_pk
          paramType: path
          description: Job primary key
          type: integer
          format: int32
        - name: pk
          paramType: path
          description: Image primary key
          type: integer
          format: int32
        responseMessages:
          - code: 200
            message: Everything is ok. Image info returned
          - code: 404
            message: Job or Image not found
        """
        return super(ImageInfoViewSet, self).retrieve(request, *args, **kwargs)
