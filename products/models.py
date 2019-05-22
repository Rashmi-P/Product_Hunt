from django.db import models
from datetime import datetime                                         
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    put_date = models.DateTimeField(default=datetime.now, blank=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    body = models.TextField(max_length=500)
    url = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

    def altered_pubdate(self):
        return self.put_date.strftime('%b %e %Y')



    