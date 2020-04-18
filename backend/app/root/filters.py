from django.db.models import Q
import django_filters
from .models import Category, Banner, PostBaseInfo


class CategoryFilter(django_filters.rest_framework.FilterSet):
    """
    Category Filter
    """
    level_min = django_filters.NumberFilter(field_name='category_level', lookup_expr='gte')
    level_max = django_filters.NumberFilter(field_name='category_level', lookup_expr='lte')

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(id=value) | Q(parent_category_id=value) | Q(
            parent_category__parent_category_id=value))

    class Meta:
        model =   Category
        fields = ['id', 'level_min', 'level_max', 'is_tab']


class BannerFilter(django_filters.rest_framework.FilterSet):
    """
    Banner Filter
    """
    level_min = django_filters.NumberFilter(field_name='category_level', lookup_expr='gte')
    level_max = django_filters.NumberFilter(field_name='category_level', lookup_expr='lte')

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Banner
        fields = ['title', 'url', 'index']


class PostBaseInfoFilter(django_filters.rest_framework.FilterSet):
    """
    Base Post Currently filtering on Time Created
    """
    time_min = django_filters.DateFilter(field_name='add_time', lookup_expr='gte')
    time_max = django_filters.DateFilter(field_name='add_time', lookup_expr='lte')

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = PostBaseInfo
        fields = ['time_min', 'time_max', 'is_hot', 'is_recommend', 'post_type']
