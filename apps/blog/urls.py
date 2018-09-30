from django.urls import path, include
from . import views
from blog.views_base import BlogsListViewSet
from rest_framework.routers import DefaultRouter

app_name = 'blog'

router = DefaultRouter()
# 配置resource的URL
router.register(r'search_blogs', BlogsListViewSet)

urlpatterns = [
    # 获取所有工具类别
    path('cate', views.get_blog_cate),
    # 通过cate获取工具列表
    path('list/<int:cate>', views.get_blog_allList),
    # 获取素材详情
    path('details/<int:id>', views.get_blog_details),
    # 获取素材详情的下载链接
    #path('download/<int:id>', views.get_tools_cloud),
    # 文章访问量统计
    path('looked_num/<int:id>', views.get_blog_looks),
    # 下载量统计
    #path('download_num/<int:id>', views.get_tools_downloads),
    # 获取最近5条文章
    path('new', views.get_new_blog),

    # DFW工具列表
    path('', include(router.urls))
]
