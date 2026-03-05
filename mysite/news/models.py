from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='news/', blank=True, null=True)
    excerpt = models.TextField(help_text='Short description shown in news listing')
    content = models.TextField()
    gallery = models.ForeignKey(
        'gallery.Gallery',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
    )
    published_date = models.DateField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class NewsSettings(models.Model):
    news_per_page = models.PositiveIntegerField(
        default=10,
        help_text='Number of articles per page in the news list',
    )

    class Meta:
        verbose_name = 'News Settings'
        verbose_name_plural = 'News Settings'

    def __str__(self):
        return f'News Settings (per page: {self.news_per_page})'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1, defaults={'news_per_page': 10})
        return obj
