# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_nested.routers import DefaultRouter

from image_downloader import views

api_v1_router = DefaultRouter()
api_v1_router.register(
    'job',
    views.JobViewSet,
    base_name='job'
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_v1_router.urls))
]
