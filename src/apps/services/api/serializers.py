from rest_framework import serializers

from .. import models


class PriceSerializerBase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Price
        fields = ['id', 'title', 'price', 'starting_from']


class PriceSerializer(PriceSerializerBase):
    prices = PriceSerializerBase(many=True)

    class Meta:
        model = models.Price
        fields = ['id', 'title', 'price', 'prices', 'starting_from']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    prices = PriceSerializer(many=True)

    class Meta:
        model = models.Service
        fields = ['id', 'title', 'image', 'prices']
