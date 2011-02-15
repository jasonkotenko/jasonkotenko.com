from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(User, related_name='posts')
  title = models.CharField(max_length=200)
  body = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  up_date = models.DateTimeField(auto_now=True)
  slug = models.CharField(max_length=200)

  def date(self):
    return self.pub_date

  def __unicode__(self):
    return self.title
    
  class META:
    ordering = ('pub_date',)
    
  
