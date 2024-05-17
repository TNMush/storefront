from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType # model for allowing generic relationships
from django.contrib.contenttypes.fields import GenericForeignKey # for viewing actual object


    
class LikedItem(models.Model):
    #who is applied to which item
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #type of object(product, video, article)- to find the table
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #id of the object to find the record
    object_id = models.IntegerField()
    
    content_id = GenericForeignKey()