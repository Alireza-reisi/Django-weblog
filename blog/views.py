from django.shortcuts import render
from . import models
# Create your views here.


def post_detail(request, title):
    article = models.article.objects.get(title=title)
    return render(request, 'article-details.html', context={'article': article})
