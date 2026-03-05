from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Article, NewsSettings


def article_list(request):
    articles = Article.objects.filter(is_published=True)
    per_page = NewsSettings.get_settings().news_per_page
    paginator = Paginator(articles, per_page)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'news/article_list.html', {'page_obj': page_obj})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'news/article_detail.html', {'article': article})
