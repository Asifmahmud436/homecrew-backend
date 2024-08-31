from django.db import models
from client.models import Client

STARS = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]
STAR_VALUES = dict(STARS)
class Service(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField()
    image = models.ImageField(upload_to='service/images/')

    def get_average_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return None
        total_rating = sum(int(STAR_VALUES.get(review.rating,'0')) for review in reviews)
        average_rating = total_rating/reviews.count() if reviews.count() > 0 else None
        return average_rating
    
    
    def __str__(self):
        return self.name
    
    

class Review(models.Model):
    # service = models.ForeignKey(Service,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=True,blank=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='reviews',null=True,blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10,choices=STARS)
    slug = models.SlugField(max_length=40,null=True,blank=True)

    def __str__(self) :
        return f"{self.client.user.first_name} {self.client.user.last_name}'s review on {self.service.name}"