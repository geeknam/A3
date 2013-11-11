from django.conf.urls import patterns, url, include

from .views import ManifestListView

urlpatterns = patterns('orders.views',
    url(r'^$', ManifestListView.as_view(), name='manifest_list'),
)