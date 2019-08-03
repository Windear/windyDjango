from .models import Resources
from .serializers import ResourcesSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import CateFilter


# 分页配置
class ResourcesPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# 返回接口
class ResourcesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    素材列表页，模糊搜索功能
    """
    queryset = Resources.objects.all().order_by("-createtime")
    # 返回序列化数据
    serializer_class = ResourcesSerializer
    # 分页配置
    pagination_class = ResourcesPagination
    # 模糊查询
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', 'introduction', 'tag', 'file_type')


# 返回接口
class ResourcesListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    素材列表页，模糊搜索功能
    """
    queryset = Resources.objects.all().order_by("-createtime")
    # 返回序列化数据
    serializer_class = ResourcesSerializer
    # 分页配置
    pagination_class = ResourcesPagination
    # 模糊查询
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('=tag', 'file_type')


# 类别筛选
class ResourcesListViewCate(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    类别筛选
    """
    queryset = Resources.objects.all().order_by("-createtime")
    # 返回序列化数据
    serializer_class = ResourcesSerializer
    # 分页配置
    pagination_class = ResourcesPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['=cate']

    # # 查询分类
    # def get_queryset(self):
    #     queryset = Resources.objects.all().order_by("-createtime")
    #     cate = self.request.query_params.get("cate", 0)
    #     if cate:
    #         queryset = queryset.filter(cate=int(cate))
    #     return queryset


# 类别筛选格式
class ResourcesListViewCateFormat(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    类别筛选格式
    """
    queryset = Resources.objects.all().order_by("-createtime")
    # 返回序列化数据
    serializer_class = ResourcesSerializer
    # 分页配置
    pagination_class = ResourcesPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CateFilter
    # search_fields = ['=cate']
