from django.contrib import admin

from ibebeapp.models import Product, Brand, Category


class CategoryInlineAdmin(admin.TabularInline):
    model = Category


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInlineAdmin
    ]


admin.site.register(Product)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category)
