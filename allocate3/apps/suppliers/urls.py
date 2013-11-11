from django.conf.urls import patterns, url, include

from .views import SupplierListView, SupplierDetailView

urlpatterns = patterns('suppliers.views',
    url(r'^$', SupplierListView.as_view(), name='supplier-list'),
    url(r'^(?P<slug>[-\w.]+)/$', SupplierDetailView.as_view(), name='supplier-detail')
)