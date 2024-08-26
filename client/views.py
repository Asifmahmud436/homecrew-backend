from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer