from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
]
