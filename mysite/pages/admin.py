from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'order', 'gallery', 'updated_at']
    list_filter = ['is_published']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'order']
    fields = ['title', 'slug', 'content', 'featured_image', 'gallery',
              'meta_description', 'show_news', 'is_published', 'show_in_menu', 'order']
