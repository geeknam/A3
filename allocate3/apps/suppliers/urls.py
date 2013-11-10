from django.conf.urls import patterns, url, include

from .views import SupplierListView

urlpatterns = patterns('suppliers.views',
    url(r'^$', SupplierListView.as_view(), name='product_list'),
)