from django.contrib import admin

from products.models import ProductCategory, Product

#admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProudctAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','category')
    fields = ('image','name','description',('price','quantity'),'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


