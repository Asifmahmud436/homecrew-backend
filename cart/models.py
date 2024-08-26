from django.db import models
from client.models import Client
from service.models import Service

ORDER_TYPE = [
    ('Bought','Bought'),
    ('Ordered','Ordered'),
    
]

class Cart(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    order_status = models.CharField(max_length=10,choices=ORDER_TYPE)
    cancel = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.client.user.first_name} ordered {self.service.name}"

