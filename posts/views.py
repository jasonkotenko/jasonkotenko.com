from django.http import HttpResponse
from jasonkotenko.posts.models import Post
from django.shortcuts import get_list_or_404, render_to_response, get_object_or_404

def latest(request):
	a = sorted(get_list_or_404(Post), key=Post.date, reverse=True)
	return render_to_response('posts/post_list.html', \
                                   {'post_list': a})
                                   
def post(request, req_name):
    p = get_object_or_404(Post, slug=req_name)
    return render_to_response('posts/post_detail.html', \
                                    {'object': p})                              
