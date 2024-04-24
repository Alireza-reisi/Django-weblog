from django.shortcuts import render
from blog.models import article


# Create your views here.


def home(request):
    articles = article.objects.filter(published=True)
    return render(request, 'index.html', context={'articles': articles})
