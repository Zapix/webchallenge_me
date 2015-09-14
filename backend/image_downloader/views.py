# -*- coding: utf-8 -*-
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
