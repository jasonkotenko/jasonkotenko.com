from django.contrib.syndication.views import Feed
from jasonkotenko.posts.models import Post

class PostFeed(Feed):
  title = "Jason Kotenko's Blog"
  link = "/"
  description = "Technical and personal musings of Jason Kotenko"
  description_template = 'feeds/post_description.html'
  
  def items(self):
    return Post.objects.order_by('-pub_date')[:5]

  def item_title(self, item):
    return item.title

  def item_description(self, item):
    return item.body

  def item_link(self, item):
    return "/posts/" + item.slug
