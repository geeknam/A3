from django.conf.urls import patterns, url, include

from .views import ProductDetailView, ProductListView

urlpatterns = patterns('products.views',
    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<code>[-\w.]+)/$', ProductDetailView.as_view(), name='product-detail'),
)