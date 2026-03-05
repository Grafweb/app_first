from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Galleries'
        ordering = ['name']

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery/')
    alt = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.gallery.name} - {self.alt or self.image.name}"
