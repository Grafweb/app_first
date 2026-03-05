from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Page


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    context = {'page': page}

    if page.show_news in ('featured', 'full'):
        from news.models import Article, NewsSettings
        articles = Article.objects.filter(is_published=True)
        if page.show_news == 'featured':
            context['news_articles'] = articles[:3]
        else:
            per_page = NewsSettings.get_settings().news_per_page
            paginator = Paginator(articles, per_page)
            context['news_page_obj'] = paginator.get_page(request.GET.get('page'))

    return render(request, 'pages/page_detail.html', context)
