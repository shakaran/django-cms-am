from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('customers.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico')))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

