from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('stock',)


admin.site.register(Producto, ProductoAdmin)