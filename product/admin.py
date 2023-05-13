from django.contrib import admin

# Register your models here.

from product.models import Category, Product, Review, Tag

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Tag)
