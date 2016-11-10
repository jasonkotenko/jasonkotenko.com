from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag, TaggedItem
from random import sample
from django.db import connection, transaction

class Post(models.Model):
  author = models.ForeignKey(User, related_name='posts')
  title = models.CharField(max_length=200)
  body = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  up_date = models.DateTimeField(auto_now=True)
  slug = models.CharField(max_length=200)
  tags = TagField()

  def save(self, *args, **kwargs):
    super(Post, self).save(*args, **kwargs)
    cursor = connection.cursor()
    cursor.execute("update posts_post set tsv = setweight(to_tsvector('english', coalesce(tags,'')), 'A') || setweight(to_tsvector('english', coalesce(title,'')), 'B') || setweight(to_tsvector('english', coalesce(body,'')), 'C');")
    transaction.commit_unless_managed()
    
  def get_similar(self):
    #similar = map(lambda t: TaggedItem.objects.get_by_model(Post,t), 
    #                  self.get_tags())
    #return similar
    return TaggedItem.objects.get_related(self, Post)    

  def date(self):
    return self.pub_date

  def __unicode__(self):
    return self.title
    
  class META:
    ordering = ('pub_date',)
    
  
