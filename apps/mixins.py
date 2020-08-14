from django.db import models
from rest_framework import viewsets


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class DefaultViewSetMixin(object):
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class ModelViewSetMixin(viewsets.ModelViewSet):
    pass
