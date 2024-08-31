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
    client = serializers.SerializerMethodField()
    service = serializers.PrimaryKeyRelatedField(queryset=models.Service.objects.all())

    class Meta:
        model = models.Review
        fields = '__all__'

    def get_client(self, obj):
        # Accessing the username from the related User model through the Client model
        return obj.client.user.username if obj.client and obj.client.user else None