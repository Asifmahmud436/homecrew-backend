from rest_framework import serializers
from django.contrib.auth.models import User
from .import models

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Client
        fields = '__all__'