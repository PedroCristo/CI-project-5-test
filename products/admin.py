from django.contrib import admin
from .models import Product, Category, Gender_category, Product_status
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'gender_category',
        'old_price',
        'price',
        'rating',
        'product_status',
        'featured',
    )
    summernote_fields = ('description, watch_details,  features')
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Gender_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Product_statusAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )    


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gender_category, CategoryAdmin)
admin.site.register(Product_status, CategoryAdmin)
