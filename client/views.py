from django.shortcuts import render,redirect
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from client.models import Client

class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        return queryset
        

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            Client.objects.create(user=user, facebook_Id_link='')
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://homecrew-backend.vercel.app/client/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            try:
                user2 = User._default_manager.get(username=username)
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user2 = None
            
            if user2 is not None:
                if user2.is_active:
                    if user is not None:
                        token, _ = Token.objects.get_or_create(user=user)
                        login(request, user)
                        return Response({'token': token.key, 'user_id': user.id})
                    else:
                        return Response({'error': "Invalid password. Please try again."})
                else:
                    return Response(
                        {'error': "Your account is not activated. Please check your email for the activation link."}
                    )
            else:
                return Response(
                    {'error': "Invalid Username. Please try again."}
                )
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    
