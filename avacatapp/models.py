from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import ResourceIndex

class Resource(models.Model):
   name = models.CharField(max_length=200)
   value =  models.TextField(max_length=8000)
   link = models.CharField(max_length=500, blank=True)
   created_date = models.DateField(default=timezone.now)
   image = models.ImageField(upload_to = "images", default = 'images/placeholder.png')
   last_modified_by = models.ForeignKey(User)
   likes = models.IntegerField(default=0)
   view_count = models.IntegerField(default=0)
   is_liked_by_user = models.BooleanField(default=False)


class Like(models.Model):
    user = models.ForeignKey(User)
    resource = models.ForeignKey(Resource)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, user, resource ):
        like = cls(user=user, resource = resource)
        like.save()
        return like

    @classmethod
    def remove(cls, user, resource ):
        like = Like.objects.get(user=user, resource = resource)
        like.delete()
        return like
