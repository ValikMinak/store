from django.contrib import admin
from django.utils.safestring import mark_safe

from items.models import Item, Category


class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50px>')
        return '-'

    get_photo.short_description = 'Фото'


class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'description')


admin.site.register(Item, AdminItem)
admin.site.register(Category, AdminCategory)
