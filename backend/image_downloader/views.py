# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from . import models
from . import serializers


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobSerializer

    def get_queryset(self):
        return models.Job.objects.all()

    def update(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)


class ImageInfoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImageInfoSerializer

    def get_job(self):
        return get_object_or_404(
            models.Job,
            pk=self.kwargs['job_pk']
        )

    def get_queryset(self):
        return self.get_job().images.all()

    def create(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)
