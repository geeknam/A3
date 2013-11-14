from rest_framework import viewsets

from .models import Company
from .serializers import CompanySerializer
from styles.utils import create_classes_from_request


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class BreadcrumbsMixin(object):

    def dispatch(self, request, *args, **kwargs):
        app_class = create_classes_from_request(request)[0]
        breadcrumbs = [
            (app_class.title(), '/%s/' % app_class)
        ]
        other_breadcrumbs = self.get_breadcrumbs(*args, **kwargs)
        if other_breadcrumbs:
            breadcrumbs.extend(other_breadcrumbs)
        request.breadcrumbs(breadcrumbs)
        # request.show_breadcrumbs = True
        return super(BreadcrumbsMixin, self).dispatch(request, *args, **kwargs)

    def get_breadcrumbs(self, *args, **kwargs):
        return None
