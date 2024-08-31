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
    client = serializers.SlugRelatedField(slug_field='username', queryset=models.Client.objects.all())
    service = serializers.PrimaryKeyRelatedField(queryset=models.Service.objects.all())

    class Meta:
        model = models.Review
        fields = '__all__'