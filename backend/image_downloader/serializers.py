# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import models


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Job


class ImageInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ImageInfo
        exclude = ('job', )
