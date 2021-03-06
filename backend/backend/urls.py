# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter

from image_downloader import views

api_v1_router = DefaultRouter()
api_v1_router.register(
    'job',
    views.JobViewSet,
    base_name='job'
)

api_v1_job_router = NestedSimpleRouter(
    api_v1_router,
    'job',
    lookup='job'
)
api_v1_job_router.register(
    'image',
    views.ImageInfoViewSet,
    base_name='image'
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_v1_router.urls)),
    url(r'^api/v1/', include(api_v1_job_router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        )
    ]
