from django.contrib import admin
from django.urls import path, include
from .views import saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('', include('core.urls', namespace='core')),
]