from django.conf.urls.defaults import *
from jasonkotenko.posts.models import Post
from jasonkotenko.feeds import PostFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

queryset = {'queryset': Post.objects.all()}

urlpatterns = patterns('',
    # Example:
    #(r'^$', 'django.views.generic.list_detail.object_list', queryset),
    url(r'^$', 'jasonkotenko.posts.views.latest', name="latest_posts"),
    url(r'^tinymce/', include('tinymce.urls'), name="tinymce"),
    url(r'^posts/feed/$', PostFeed(), name="posts_feed"),
    url(r'^posts/(?P<req_name>.*)/$', 'jasonkotenko.posts.views.post', name="single_post"),
    url(r'^articles/(?P<req_name>.*)/$', 'jasonkotenko.articles.views.article', name="single_article"),
    url(r'^library/(?P<req_name>.*)/$', 'jasonkotenko.library.views.show_library', "library"),
    url(r'^gallery/(?P<req_name>.*)/$', 'jasonkotenko.photos.views.gallery', name="single_photo_gallery"),
    url(r'^photos/$', 'jasonkotenko.photos.views.gallery_list', name="photo_gallery_list"),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
from django.views.static import serve
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', serve, {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
    )
