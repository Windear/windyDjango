from django.urls import path, include, re_path
from . import views
from resources.views_base import ResourcesListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# 配置resource的URL
router.register(r'search_resources', ResourcesListViewSet)

app_name = 'resources'
urlpatterns = [
    # 所有类别
    path('cate', views.get_resources_cate),
    # 获取素材列表
    path('list/<int:cate>', views.get_resources_list),
    # 获取素材详情
    path('details/<int:id>', views.get_resources_details),
    # 获取素材详情的下载链接
    path('cloud/<int:id>', views.get_resources_cloud),
    # 访问量统计
    path('looked_num/<int:id>', views.get_resources_looks),
    # 下载量统计
    path('download_num/<int:id>', views.get_resources_downloads),
    # 返回格式列表
    path('format', views.get_resources_format),
    # 获取素材分类列表
    path('type', views.get_resources_format_list),
    # 获取最近8条素材
    path('new', views.get_new_resources),

    # DFW素材列表
    path('', include(router.urls))
]
