from decimal import Decimal

from django.db import models

from django_countries import CountryField
from core.base import SlugUniqueMixin, AddressMixin


class Supplier(SlugUniqueMixin, AddressMixin, models.Model):
    '''
    Base model for supplier objects
    '''
    name = models.CharField('Codename',
        unique=True, max_length=200, db_index=True)
    email = models.EmailField('Default email address',
        help_text='All system generated emails will be sent to this address as well as the nominated users.')
    invoice_disclaimer = models.TextField(null=True, blank=True,
        help_text='Will be displayed on the supplier\'s customer invoice template. Supports HTML markup.')
    score = models.DecimalField(max_digits=4, decimal_places=3, default=1.00,
        help_text='Affects a supplier\'s ability to win a bid. If a supplier has a score of 0.97 and they bid $97.00 their bid will be calculated as $100.00 when comparing with other suppliers. A supplier with 0.99 will beat a supplier with 0.97 if the bid amount is equal.')
    colour = models.CharField(max_length=30, default='#000099',
        help_text='CSS colour code to be used with this supplier. Hex codes are preferable.'
    )
    # allowed_currencies = models.ManyToManyField('payments.Currency',
    #     null=True, blank=True, related_name='+',
    #     help_text='Currencies which this supplier is allowed to bid in.')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        permissions = (
            ('view_supplier', 'Can view suppliers'),
            ('view_internal', 'Can view internal information like supplier score'),
        )

    def score_price(self, price=1):
        '''
        Return a price based on the supplier's score - so if score_price is called for
        $100.00 and the score is 0.97 then the score price will return as $103.09
        '''
        # convert price and score to decimal (should already be, but could potentially be float)
        price = Decimal(price)
        score = Decimal(self.score)
        score_price = price / score    # calculate score price
        return score_price.quantize(Decimal(10) ** -2)  # return rounded to 2 decimals

    @models.permalink
    def get_absolute_url(self):
        return ('supplier-detail', (), {
            'slug': self.slug,
        })

# @receiver(post_save, sender=Supplier)
# def allow_supplier_ship_all_products(instance=None, created=False, **kwargs):
#     if created:
#         add_supplier_to_product_allowed_suppliers.delay(instance)
