
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('app.product.urls')),
    path('admin/', admin.site.urls),
    path('khalti/', include('app.khalti.urls')),
    path('esewa/', include('app.esewa.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)