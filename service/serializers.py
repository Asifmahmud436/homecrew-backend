from rest_framework import serializers
from .import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField(many = False)
    client = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Review
        fields = '__all__'