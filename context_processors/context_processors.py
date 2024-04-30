from blog.models import article, Category


def recent_articles(request):
    last_articles = article.objects.order_by('-pub_date')[:5]
    return {'recent_articles': last_articles}


def best_categories(request):
    categories = Category.objects.all()[:5]
    return {'categories': categories}