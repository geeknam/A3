from django.conf.urls import patterns, url, include

from .views import ManifestListView, ManifestCreateView

urlpatterns = patterns('orders.views',
    url(r'^$', ManifestListView.as_view(), name='manifest_list'),
    url(r'^create/', ManifestCreateView.as_view(), name='manifest_create'),
)