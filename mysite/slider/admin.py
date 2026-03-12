from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, SliderImage


class SliderImageInline(admin.StackedInline):
    model = SliderImage
    extra = 1
    readonly_fields = ('preview',)
    fields = ('preview', 'image', 'alt', 'order', 'link_type', 'page_link', 'article_link', 'external_url', 'link_new_tab')

    class Media:
        js = ('slider/admin_inline.js',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:100px; max-width:240px; object-fit:cover; border-radius:4px;">',
                obj.image.url,
            )
        return '-'
    preview.short_description = 'Preview'


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'show_on_home', 'show_on_all_pages', 'show_on_all_news', 'image_count')
    list_editable = ('is_active',)
    filter_horizontal = ('pages', 'articles')
    fieldsets = (
        (None, {
            'fields': ('name', 'is_active'),
        }),
        ('Display on', {
            'fields': ('show_on_home', 'show_on_all_pages', 'show_on_all_news'),
            'description': 'Select where this slider appears globally.',
        }),
        ('Specific pages / articles', {
            'fields': ('pages', 'articles'),
            'description': 'Assign slider to specific pages or articles. Specific assignments override global settings.',
        }),
    )
    inlines = [SliderImageInline]

    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'
