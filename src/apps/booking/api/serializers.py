from rest_framework import serializers

from .. import models


class FormFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FormFeedback
        fields = '__all__'


class FormPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FormPhone
        fields = '__all__'


class BookingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookingSession
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'

    session = serializers.PrimaryKeyRelatedField(queryset=models.BookingSession.objects.all()) # noqa
