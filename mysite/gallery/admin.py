from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    readonly_fields = ['preview']
    fields = ['preview', 'image', 'alt', 'order']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:80px;width:auto;border-radius:4px;" />', obj.image.url)
        return '-'
    preview.short_description = 'Preview'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalleryImageInline]
