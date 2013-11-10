from django.db import models
from core.base import AddressMixin



class Company(AddressMixin, models.Model):
    name = models.CharField(max_length=200, help_text='Mainly for internal use.')
    display_name = models.CharField(max_length=200,
        help_text='For official documents produced by this company.')
    company_number = models.CharField(max_length=200, null=True, blank=True,
        help_text='ABN/ACN/CRN etc')
    logo = models.ImageField(upload_to='core/company', null=True, blank=True)
    # default_sell_currency = models.ForeignKey(
    #     'payments.Currency',
    # )
    supplier_email = models.EmailField()
    supplier_email_name = models.CharField(max_length=200, null=True, blank=True)
    customer_email = models.EmailField()
    customer_email_name = models.CharField(max_length=200, null=True, blank=True)
    transactional_bcc_email = models.EmailField(null=True, blank=True,
        help_text='Customer bulk emails will Bcc this address')