from rest_framework import serializers
from .models import Store, StoreGroup


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class StoreGroupSerializer(serializers.ModelSerializer):
    stores = StoreSerializer(many=True)
    class Meta:
        model = StoreGroup
        fields = '__all__'