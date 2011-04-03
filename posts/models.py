from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag

class Post(models.Model):
  author = models.ForeignKey(User, related_name='posts')
  title = models.CharField(max_length=200)
  body = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  up_date = models.DateTimeField(auto_now=True)
  slug = models.CharField(max_length=200)
  tags = TagField()
  
  def get_tags(self):
    return Tag.objects.get_for_object(self)

  def date(self):
    return self.pub_date

  def __unicode__(self):
    return self.title
    
  class META:
    ordering = ('pub_date',)
    
  
