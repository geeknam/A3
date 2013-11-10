from django.db import models
from core import base

class Product(models.Model):
    '''
    Base product object used internally by purchaser
    '''
    code = models.CharField(max_length=300, unique=True, db_index=True)
    name = models.CharField(max_length=300, unique=True, db_index=True)
    weight = models.DecimalField(
        'Shipping Weight', max_digits=20, decimal_places=3, null=True, blank=True, default='0.0',
        help_text='Nominal product shipping weight (in kg). This can be overridden by suppliers.')
    requires_serial_number = models.BooleanField(default=True,
        help_text='This should be true for any non-accessory products.')
    allowed_suppliers = models.ManyToManyField('suppliers.Supplier', null=True, blank=True,
        related_name='allowed_products')
    packing_comment = models.CharField(max_length=300, null=True, blank=True)
    bundle = models.ForeignKey('Bundle', null=True, blank=True, default=None)

    class Meta:
        ordering = ['code']

    @models.permalink
    def get_absolute_url(self):
        return ('product-detail', (), {
            'code': self.code.lower(),
        })

class Bundle(models.Model):

    title = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='bundled_products')

    def __unicode__(self):
        return self.title


class SupplierProduct(models.Model):
    code = models.CharField(max_length=300, db_index=True, null=True, blank=True)
    weight = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True,
        help_text='Supplier shipping weight.')
    supplier = models.ForeignKey('suppliers.Supplier', related_name='products')
    product = models.ForeignKey('Product')
    # objects = SupplierProductManager()

    class Meta:
        ordering = ['product__code', 'supplier__name']
        unique_together = (
            # only create 1 sp per supplier/product!
            ('supplier', 'product'),
            # don't let suppliers duplicate skus
            # ('supplier', 'code')
        )

class Inventory(models.Model):
    '''
    Allows for the allocation of pre-paid stock while confirming an order
    This will be allocated ahead of quotes before the manifest is even opened for bidding
    '''
    product = models.ForeignKey('Product')
    supplier = models.ForeignKey('suppliers.Supplier')
    quantity = models.IntegerField(default=0)
    price = base.PriceField()
    date = models.DateTimeField('Date purchased')
    company = models.ForeignKey('core.Company')
    # currency = models.ForeignKey('payments.Currency')

    # objects = InventoryManager()

    # def get_absolute_url(self):
    #     return reverse('products.views.inventory_detail', args=[self.pk])

    def __unicode__(self):
        return '%s - %s' % (self.product.code, self.supplier.name)

    @property
    def quantity_remaining(self):
        quantity_used = self.invoiceline_set.filter(active=True).aggregate(models.Sum('quantity'))['quantity__sum']  # get used quantity
        if not quantity_used:
            quantity_used = 0
        return self.quantity - quantity_used

    class Meta:
        ordering = ['pk']
        verbose_name = 'Prepaid Inventory'


# class UsedSerialNumber(models.Model):
#     '''
#     Model to ensure suppliers do not reuse serial numbers
#     '''
#     serial_number = models.CharField(
#         max_length=300, null=True, blank=True, default='', db_index=True)
#     supplier = models.ForeignKey('suppliers.Supplier')
#     invoice = models.ForeignKey('orders.Invoice')

#     def __unicode__(self):
#         return self.serial_number