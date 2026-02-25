from .models import Page


def menu_pages(request):
    return {
        'menu_pages': Page.objects.filter(is_published=True, show_in_menu=True)
    }
