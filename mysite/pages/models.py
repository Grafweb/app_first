from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='pages/', blank=True, null=True)
    gallery = models.ForeignKey(
        'gallery.Gallery',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pages',
    )
    meta_description = models.CharField(max_length=160, blank=True)
    is_published = models.BooleanField(default=False)
    show_in_menu = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    NEWS_DISPLAY_CHOICES = [
        ('none', 'No news'),
        ('featured', 'Featured - 3 latest articles'),
        ('full', 'Full list with pagination'),
    ]
    show_news = models.CharField(
        max_length=20,
        choices=NEWS_DISPLAY_CHOICES,
        default='none',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})
