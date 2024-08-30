from rest_framework import serializers
from django.contrib.auth.models import User
from .import models

class Usererializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class ClientSerializer(serializers.ModelSerializer):
    user = Usererializer(read_only = True)
    # user = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Client
        fields = '__all__'

    def update(self, instance, validated_data):
        # Handle nested update for User fields
        user_data = validated_data.pop('user', None)
        # if user_data:
        #     user = instance.user
        #     user.username = user_data.get('username', user.username)
        #     user.first_name = user_data.get('first_name', user.first_name)
        #     user.last_name = user_data.get('last_name', user.last_name)
        #     user.email = user_data.get('email', user.email)
        #     user.save()
        
        # Update Client fields
        instance.user.username = validated_data.get('username', instance.user.username)
        instance.user.first_name = validated_data.get('first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get('last_name', instance.user.last_name)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.facebook_Id_link = validated_data.get('facebook_Id_link', instance.facebook_Id_link)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

# class MakeAdminSerializer(serializers.ModelSerializer):
#     # is_staff = serializers.BooleanField()
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'is_staff', 'first_name', 'last_name']

#     def update(self, instance, validated_data):
#         request_user = self.context['request'].user
        
#         # If the user is not an admin, remove the is_staff field from validated_data
#         if not request_user.is_staff and 'is_staff' in validated_data:
#             validated_data.pop('is_staff')
        
#         # Proceed with the regular update process
#         return super().update(instance, validated_data)
