from django.db import models
from client.models import Client

STARS = [
    ('one','✩'),
    ('two','✩✩'),
    ('three','✩✩✩'),
    ('four','✩✩✩✩'),
    ('five','✩✩✩✩✩'),
]
class Service(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField()
    image = models.ImageField(upload_to='service/images/')

    def __str__(self):
        return self.name
    

class Review(models.Model):
    # service = models.ForeignKey(Service,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=True,blank=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10,choices=STARS)
    slug = models.SlugField(max_length=40)

    def __str__(self) :
        return f"{self.client.user.first_name}'s review on {self.service.name}"