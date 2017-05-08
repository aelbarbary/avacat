from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import ResourceIndex

# Create your models here.

# Blogpost to be indexed into ElasticSearch
class Resource(models.Model):
   name = models.CharField(max_length=200)
   value =  models.CharField(max_length=8000)
   link = models.CharField(max_length=500, blank=True)
   created_date = models.DateField(default=timezone.now)
   image = models.ImageField(upload_to = "images", default = 'images/placeholder.png')
   likes = models.IntegerField(default = 0)
   dislikes = models.IntegerField(default = 0)

   def indexing(self):
       obj = ResourceIndex(
          meta={'id': self.id},
          name=self.name,
          created_date =self.created_date,
          description=self.description,
        #   image=self.image,
          link = self.link
       )
       obj.save()
       return obj.to_dict(include_meta=True)
