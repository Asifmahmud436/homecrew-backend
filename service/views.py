from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework import filters
from django.db.models import Avg
from django.core.exceptions import PermissionDenied
from django.db.models import Avg, IntegerField
from django.db.models.functions import Cast



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
    serializer_class = serializers.ServiceSerializer

    def get_queryset(self):
        queryset = models.Service.objects.all()
        queryset = queryset.annotate(
            average_rating=Avg(Cast('reviews__rating', IntegerField()))
        )

        queryset = queryset.order_by('-average_rating')
        
        return queryset
    