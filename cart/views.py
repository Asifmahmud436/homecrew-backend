from django.shortcuts import render
from rest_framework import viewsets
from .import serializers
from .import models

class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        client_id = self.request.query_params.get('client_id')
        client_username = self.request.query_params.get('client_username')
        if client_id:
            queryset = queryset.filter(client_id=client_id)
        if client_username:
            queryset = queryset.filter(client__user__username__icontains=client_username)
        return queryset
    