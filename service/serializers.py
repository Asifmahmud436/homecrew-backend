from rest_framework import serializers
from .import models

class ServiceSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = models.Service
        fields = '__all__'

    def get_average_rating(self,obj):
        return obj.get_average_rating()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'