# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Job
        read_only_fields = ('state',)


class ImageInfoSerializer(serializers.ModelSerializer):
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    size = serializers.IntegerField()
    filename = serializers.CharField()
    path = serializers.CharField()
    mimetype = serializers.CharField()

    class Meta:
        model = models.ImageInfo
        exclude = ('job', )
