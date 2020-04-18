import django_filters
from .models import  SiteInfo


class SiteInfoFilter(django_filters.rest_framework.FilterSet):
    """
    to check Website Live Status
    """
    class Meta:
        model = SiteInfo
        fields = ['is_live']


