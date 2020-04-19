from django.db.models import Q
import django_filters
from .models import ArticleInfo


class ArticleFilter(django_filters.rest_framework.FilterSet):

    time_min = django_filters.DateFilter(field_name='add_time', lookup_expr='gte')
    time_max = django_filters.DateFilter(field_name='add_time', lookup_expr='lte')

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = ArticleInfo
        fields = ['time_min', 'time_max', 'is_hot', 'is_recommend', 'is_banner']
