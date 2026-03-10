from django.contrib import admin
from django.utils.html import format_html
from .models import Article, NewsSettings


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'is_published', 'created_at']
    list_filter = ['is_published', 'published_date']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']
    readonly_fields = ['thumbnail_preview']
    fields = ['title', 'slug', 'thumbnail', 'thumbnail_preview', 'excerpt', 'content', 'gallery', 'published_date', 'is_published', 'show_contact_form']
    date_hierarchy = 'published_date'

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 400px; border-radius: 6px;" />',
                obj.thumbnail.url,
            )
        return '-'
    thumbnail_preview.short_description = 'Preview'


@admin.register(NewsSettings)
class NewsSettingsAdmin(admin.ModelAdmin):
    fields = ['news_per_page']

    def has_add_permission(self, request):
        return not NewsSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
