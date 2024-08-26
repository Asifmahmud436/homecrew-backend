from django.contrib import admin
from client.models import Client
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name','phone_no','image']

    def first_name(self,obj):
        return obj.user.first_name

admin.site.register(Client,ClientAdmin)