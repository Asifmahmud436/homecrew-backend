from django.contrib import admin
from cart.models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ['client','service','order_status','cancel']

    def client(self,obj):
        return obj.client.user.first_name
    def service(self,obj):
        return obj.service.name

admin.site.register(Cart,CartAdmin)