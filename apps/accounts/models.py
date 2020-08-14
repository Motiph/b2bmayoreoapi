from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from apps.mixins import TimeStampModel
from apps.core.models import StoreGroup, Store


class Profile(TimeStampModel):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(StoreGroup, blank=True)
    main_store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username



class Order(TimeStampModel):
    items = models.CharField(max_length=6000)
    store = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField( max_digits=19, decimal_places=2)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

