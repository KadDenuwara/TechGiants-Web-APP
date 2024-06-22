from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import order_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('newsletter/', include('newsletter.urls')),
    path('order-history/', order_history, name='order_history'),
]

#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATICFILES_DIRS[0])
urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
