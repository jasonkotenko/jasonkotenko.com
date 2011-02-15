from django.db import models

class Article(models.Model):
	name = models.CharField(max_length=200)
	content = models.TextField()
	description = models.TextField()
	keywords = models.TextField() #comma-delimited list of keywords for search engines
	last_modified = models.DateField(auto_now=True)
	slug = models.SlugField()
	
	def __unicode__(self):
		return self.name
	
	
