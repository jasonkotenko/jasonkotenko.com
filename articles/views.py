from django.http import HttpResponse
from jasonkotenko.articles.models import Article
from django.shortcuts import get_object_or_404, render_to_response

def article(request, req_name='about-us'):
	a = get_object_or_404(Article, slug=req_name)
	return render_to_response('articles/article.html', \
                                   {'article': a})
