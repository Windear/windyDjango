from django.urls import path, include
from . import views
from macTools.views_base import ToolsListViewSet
from rest_framework.routers import DefaultRouter

app_name = 'tools'

router = DefaultRouter()

# 配置resource的URL
router.register(r'search_tools', ToolsListViewSet)

urlpatterns = [
    # 获取所有工具类别
    path('cate', views.get_tools_cate),
    # 通过cate获取工具列表
    path('list/<int:cate>', views.get_tools_allList),
    # 获取素材详情
    path('details/<int:id>', views.get_tools_details),
    # 获取素材详情的下载链接
    path('download/<int:id>', views.get_tools_cloud),
    # 访问量统计
    path('looked_num/<int:id>', views.get_tools_looks),
    # 下载量统计
    path('download_num/<int:id>', views.get_tools_downloads),
    # 获取最近6条工具列表
    path('new', views.get_new_tools),

    # DFW工具列表
    path('', include(router.urls))
]
