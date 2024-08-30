from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('list',views.ClientViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'users',views.MakeAdminViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    # path('make_admin/', views.MakeAdminView, name='make_admin'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
]