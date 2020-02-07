from django.contrib import admin
from .models import *


admin.site.register(Product)
admin.site.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'categories')
#     search_fields = ('title',)
#     list_filter = ('title',)
#
#
# admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'available', 'categories', 'created', 'updated')
#     search_fields = ('title', 'price')
#     list_filter = ('title', 'created', 'price')
