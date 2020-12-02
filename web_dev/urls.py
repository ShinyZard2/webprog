from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from products import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('bmi/', include('bmi.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

