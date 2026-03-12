from .models import Slider


def active_slider(request):
    resolver = getattr(request, 'resolver_match', None)
    if not resolver:
        return {}

    view_name = resolver.view_name
    kwargs = resolver.kwargs
    slider = None

    if view_name == 'index':
        slider = (
            Slider.objects.filter(is_active=True, show_on_home=True)
            .prefetch_related('images')
            .first()
        )

    elif view_name == 'page_detail':
        slug = kwargs.get('slug', '')
        # Specific page assignment takes priority
        slider = (
            Slider.objects.filter(is_active=True, pages__slug=slug)
            .prefetch_related('images')
            .first()
        )
        if not slider:
            slider = (
                Slider.objects.filter(is_active=True, show_on_all_pages=True)
                .prefetch_related('images')
                .first()
            )

    elif view_name == 'article_detail':
        slug = kwargs.get('slug', '')
        slider = (
            Slider.objects.filter(is_active=True, articles__slug=slug)
            .prefetch_related('images')
            .first()
        )
        if not slider:
            slider = (
                Slider.objects.filter(is_active=True, show_on_all_news=True)
                .prefetch_related('images')
                .first()
            )

    elif view_name == 'article_list':
        slider = (
            Slider.objects.filter(is_active=True, show_on_all_news=True)
            .prefetch_related('images')
            .first()
        )

    if slider:
        return {
            'active_slider': slider,
            'active_slider_images': list(slider.images.all()),
        }
    return {}
