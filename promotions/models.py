from django.db import models
from django.urls import reverse


class Promotion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='photos/promotions/%Y/%m')
    slug = models.SlugField(max_length=100, unique=True, default=None)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"
        ordering = ['-start_date']