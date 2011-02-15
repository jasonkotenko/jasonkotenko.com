from django.db import models
from jasonkotenko.posts.models import Post

# Create your models here.

class Resource(models.Model):
  title = models.CharField(max_length=256)
  URL = models.URLField()
  description = models.TextField()
  thumbnail = models.ImageField(upload_to='thumbs')
  private = models.BooleanField(default=False)
  related = models.ManyToManyField(Post, null=True, blank=True)
  
  class Meta:
    ordering = ['title']
    
  def __unicode__(self):
    return self.title

class Book(Resource):
  author = models.CharField(max_length=128)

class Technology(Resource):
  articles = models.ManyToManyField(Post, null=True, blank=True)

class Library(models.Model):
  name = models.CharField(max_length=128)
  introduction = models.TextField()
  books = models.ManyToManyField('Book', null=True, blank=True)
  articles = models.ManyToManyField(Post, null=True, blank=True)
  technologies = models.ManyToManyField('Technology', null=True, blank=True)
  
  def __unicode__(self):
    return self.name

  
