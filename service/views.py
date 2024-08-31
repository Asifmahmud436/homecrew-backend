from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework import filters
from django.db.models import Avg
from django.core.exceptions import PermissionDenied


class ReviewForService(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        service_id = request.query_params.get('service_id')
        if service_id:
            return query_set.filter(service=service_id)
        return query_set

def perform_create(self, serializer):
    if self.request.user.is_authenticated:
        try:
            client = self.request.user.client
            serializer.save(client=client)
        except models.Client.DoesNotExist:
            raise PermissionDenied("Client profile does not exist.")
    else:
        raise PermissionDenied("You must be logged in to submit a review.")

class ServiceViewSet(viewsets.ModelViewSet):
    # queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

    def get_queryset(self):
        queryset = models.Service.objects.all()
        

        queryset = queryset.annotate(
            average_rating=Avg('reviews__rating')
        )

        queryset = queryset.order_by('-average_rating')
        
        return queryset
    