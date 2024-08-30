from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='client/images/')
    phone_no = models.CharField(max_length=12)
    facebook_Id_link = models.URLField(max_length=255,validators=[URLValidator()],blank=True)

    def __str__(self):
        return f'{self.user.first_name}'