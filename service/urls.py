from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('service',views.ServiceViewSet,basename='service')
router.register('review',views.ReviewViewSet,basename='review')

urlpatterns = [
    path('',include(router.urls)),
]
