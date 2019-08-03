import django_filters
from .models import Resources


class CateFilter(django_filters.rest_framework.FilterSet):
    """
    资源类型的过滤类
    """
    cate = django_filters.NumberFilter(field_name='cate')
    file_type = django_filters.CharFilter(field_name='file_type')

    class Meta:
        model = Resources
        fields = ['cate', 'file_type']
