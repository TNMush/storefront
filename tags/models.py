from django.db import models
from django.contrib.contenttypes.models import ContentType # model for allowing generic relationships
from django.contrib.contenttypes.fields import GenericForeignKey # for viewing actual object

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    
class TaggedItem(models.Model):
    #which tag is applied to which item
    tag = models.ForeignKey(Tag, on_delete= models.CASCADE)
    #type of object(product, video, article)- to find the table
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #id of the object to find the record
    object_id = models.IntegerField()
    
    content_id = GenericForeignKey()