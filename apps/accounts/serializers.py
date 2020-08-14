from rest_framework import serializers
from .models import Profile, Order
from apps.core.serializers import StoreSerializer, StoreGroupSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    groups = StoreGroupSerializer(many=True)
    main_store = StoreSerializer()

    class Meta:
        model = Profile
        fields = '__all__'