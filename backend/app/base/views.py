from django.shortcuts import render

# Create your views here.
# _*_ coding: utf-8 _*_


from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import SiteInfo, BloggerInfo
from .serializer import BloggerInfoSerializer, SiteInfoSerializer
from .filters import SiteInfoFilter


class SiteInfoViewset(viewsets.ReadOnlyModelViewSet):
    """
    List:
    """
    queryset = SiteInfo.objects.all()
    serializer_class = SiteInfoSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SiteInfoFilter
#

class BloggerInfoViewset(viewsets.ReadOnlyModelViewSet):
    """
    List:
    """
    queryset = BloggerInfo.objects.all()
    serializer_class = BloggerInfoSerializer

