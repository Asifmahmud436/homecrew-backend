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
    client_name = serializers.CharField(source='client.user.first_name',read_only=True)
    service_name = serializers.CharField(source='service.name',read_only=True)

    class Meta:
        model = models.Review
        fields = ['id','body','created_on','rating','client_name','client','service_name','service']