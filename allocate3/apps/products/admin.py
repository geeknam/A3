from django.contrib import admin


from .models import Product, SupplierProduct, Bundle

class SupplierProductInline(admin.TabularInline):
    model = SupplierProduct
    extra = 0
    fields = [
        'supplier',
        'code',
        'weight',
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['code', 'name']

    def get_form(self, request, obj=None, **kwargs):
        '''
        Only show inlines if a product object already exists
        '''
        if obj:
            self.inlines = [SupplierProductInline]
        else:
            self.inlines = []
        return super(ProductAdmin, self).get_form(request, obj, **kwargs)


class ProductInline(admin.StackedInline):
    model = Product
    extra = 0
    fields = ['code', 'name']


class BundleAdmin(admin.ModelAdmin):
    model = Bundle
    list_display = ['title']
    filter_horizontal = ('products', )
    inlines = [ProductInline]



admin.site.register(Product, ProductAdmin)
admin.site.register(Bundle, BundleAdmin)
