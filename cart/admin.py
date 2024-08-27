from django.contrib import admin
from cart.models import Cart
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
class CartAdmin(admin.ModelAdmin):
    list_display = ['client','service','order_status','cancel']

    def client(self,obj):
        return obj.client.user.first_name
    def service(self,obj):
        return obj.service.name

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.order_status == 'Bought':
            email_subject = "You bought your order"
            email_body = render_to_string('admin_email.html', {'user' : obj.client.user,'service':obj.service})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.client.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")

admin.site.register(Cart,CartAdmin)