from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.


def article_detail(request, title):
    article = get_object_or_404(models.article, title=title)
    return render(request, 'article-details.html', context={'article': article})
