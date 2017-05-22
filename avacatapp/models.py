from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import ResourceIndex

# Create your models here.

# Blogpost to be indexed into ElasticSearch
class Resource(models.Model):
   name = models.CharField(max_length=200)
   value =  models.TextField(max_length=8000)
   link = models.CharField(max_length=500, blank=True)
   created_date = models.DateField(default=timezone.now)
   image = models.ImageField(upload_to = "images", default = 'images/placeholder.png')
   created_by_user = models.ForeignKey(User)

class Like(models.Model):
    user = models.ForeignKey(User)
    resource = models.ForeignKey(Resource)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, user, resource ):
        book = cls(user=user, resource = resource)
        book.save()
        return book
