from django.contrib import admin
from django.utils.safestring import mark_safe

from promotions.models import Promotion


class AdminPromotion(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'photo', 'start_date', 'end_date')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50px>')
        return '-'

    get_photo.short_description = 'Фото'


admin.site.register(Promotion, AdminPromotion)
