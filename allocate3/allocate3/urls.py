from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
from rest_framework import routers

from core.views import CompanyViewSet
from products.views import ProductViewSet
from suppliers.views import SupplierViewSet
from orders.views import ManifestViewSet, InvoiceViewSet, InvoiceLineViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'manifests', ManifestViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoicelines', InvoiceLineViewSet)

urlpatterns = patterns('',
    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^products/', include('products.urls')),
    url(r'^suppliers/', include('suppliers.urls')),

    # url(r'^home/$', 'core.views.home'),
    # (r'^comments/', include('django.contrib.comments.urls')),
    (r'^500/', TemplateView.as_view(template_name='500.html')),


)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(
            r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }
        )
    )