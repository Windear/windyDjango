from .models import Collection_net, Friends_net
from .serializers import collectionNetSerializer, friendsNetSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# 分页配置
class linksPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# 收藏网站
class collectionNetListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    收藏网站
    """
    queryset = Collection_net.objects.all().order_by("-id")
    # 返回序列化数据
    serializer_class = collectionNetSerializer
    # 分页配置
    pagination_class = linksPagination
    # # 模糊查询
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # search_fields = ('title', 'introduction', 'tag')


# 友情链接
class friendsNetListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    友情链接
    """
    queryset = Friends_net.objects.all().order_by("-id")
    # 返回序列化数据
    serializer_class = friendsNetSerializer
    # 分页配置
    pagination_class = linksPagination
    # # 模糊查询
