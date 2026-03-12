from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    show_on_home = models.BooleanField(
        default=False,
        help_text='Show this slider on the home page',
    )
    show_on_all_pages = models.BooleanField(
        default=False,
        help_text='Show this slider on all CMS pages (overridden by specific page assignment)',
    )
    show_on_all_news = models.BooleanField(
        default=False,
        help_text='Show this slider on the news list and all article pages (overridden by specific article assignment)',
    )
    pages = models.ManyToManyField(
        'pages.Page',
        blank=True,
        related_name='sliders',
        help_text='Show this slider on specific pages',
    )
    articles = models.ManyToManyField(
        'news.Article',
        blank=True,
        related_name='sliders',
        help_text='Show this slider on specific news articles',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    LINK_TYPE_CHOICES = [
        ('none', 'No link'),
        ('internal_page', 'Internal – Page'),
        ('internal_article', 'Internal – News article'),
        ('external', 'External URL'),
    ]

    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='slider/')
    alt = models.CharField(max_length=200, blank=True, help_text='Alt text for accessibility')
    order = models.IntegerField(default=0)

    link_type = models.CharField(
        max_length=20,
        choices=LINK_TYPE_CHOICES,
        default='none',
        help_text='Type of link attached to this image',
    )
    page_link = models.ForeignKey(
        'pages.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text='Select an internal page (used when Link type = Internal – Page)',
    )
    article_link = models.ForeignKey(
        'news.Article',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        help_text='Select a news article (used when Link type = Internal – News article)',
    )
    external_url = models.CharField(
        max_length=500,
        blank=True,
        help_text='Full URL, e.g. https://example.com (used when Link type = External URL)',
    )
    link_new_tab = models.BooleanField(
        default=False,
        help_text='Open link in a new browser tab (recommended for external links)',
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.slider.name} – image {self.order}'

    @property
    def resolved_link(self):
        if self.link_type == 'internal_page' and self.page_link_id:
            return self.page_link.get_absolute_url()
        if self.link_type == 'internal_article' and self.article_link_id:
            return self.article_link.get_absolute_url()
        if self.link_type == 'external' and self.external_url:
            return self.external_url
        return ''

    @property
    def link_target(self):
        return '_blank' if self.link_new_tab else '_self'
