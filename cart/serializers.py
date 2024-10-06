from rest_framework import serializers
from .import models

class CartSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.user.first_name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=models.Client.objects.all(), write_only=True)
    service = serializers.PrimaryKeyRelatedField(queryset=models.Service.objects.all(), write_only=True)

    class Meta:
        model = models.Cart
        fields = ['id', 'client_name', 'service_name', 'client', 'service', 'order_status', 'cancel']