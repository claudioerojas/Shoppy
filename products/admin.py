from django.contrib import admin
from .models import Product

# Register your models here.
#admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price',)
    list_display_links = ('name',)
    list_filter = ('category',)