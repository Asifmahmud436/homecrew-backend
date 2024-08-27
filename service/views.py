from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework import filters
from django.db.models import Avg


class ReviewForService(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        service_id = request.query_params.get('service_id')
        if service_id:
            return query_set.filter(service=service_id)
        return query_set

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [ReviewForService]

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
    