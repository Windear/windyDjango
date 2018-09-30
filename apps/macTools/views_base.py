from .models import Tools
from .serializers import ToolsSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# 分页配置
class ToolsPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# 返回接口
class ToolsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    素材列表页，模糊搜索功能
    """
    queryset = Tools.objects.all().order_by("-create_time")
    # 返回序列化数据
    serializer_class = ToolsSerializer
    # 分页配置
    pagination_class = ToolsPagination
    # 模糊查询
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', 'introduction', 'tag')
