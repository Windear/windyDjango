from .models import DesignWorks
from .serializers import DesginListSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# 分页配置
class DesginPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# 返回我的设计列表接口
class DesginListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    我的设计列表页，模糊搜索功能
    """
    queryset = DesignWorks.objects.all().order_by("-createtime")
    # 返回序列化数据
    serializer_class = DesginListSerializer
    # 分页配置
    pagination_class = DesginPagination
    # 模糊查询
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', 'introduction')


