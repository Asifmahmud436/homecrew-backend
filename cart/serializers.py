from rest_framework import serializers
from .import models

class CartSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(many=False)
    service = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Cart
        fields = '__all__'