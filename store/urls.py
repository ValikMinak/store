from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from orders.views import cart

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('promotions.urls', 'promotions'))),
    path('', include(('items.urls', 'items'))),
    path('', include(('orders.urls', 'orders'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),

    path('cart/', cart, name='cart'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
