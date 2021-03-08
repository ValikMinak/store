from django.db import models
from django.urls import reverse

from promotions.models import Promotion


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ['title']


class Item(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/items/%Y/%m')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    promotion = models.ForeignKey(Promotion, on_delete=models.SET_NULL, related_name='promotion_items', blank=True,
                                  null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['title']
