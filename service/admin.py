from django.contrib import admin
from service.models import Service
from service.models import Review
# Register your models here.

class ReviewModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('rating',),}

admin.site.register(Service)
admin.site.register(Review,ReviewModel)