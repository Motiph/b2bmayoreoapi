from django.db import models
from apps.mixins import TimeStampModel


class Store(TimeStampModel):
    name = models.CharField(unique=True, max_length=100)
    pace_store_id = models.CharField(unique=True, max_length=50)
    
    def __str__(self):
        return self.name

class StoreGroup(TimeStampModel):
    name = models.CharField(unique=True, max_length=100)
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name