from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "image",
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "webname",
        "name",
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
