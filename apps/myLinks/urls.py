from django.urls import path, include
from myLinks.views import collectionNetListViewSet, friendsNetListViewSet
from rest_framework.routers import DefaultRouter

app_name = 'myLinks'

router = DefaultRouter()

# 配置resource的URL
router.register(r'collection', collectionNetListViewSet)
router.register(r'friends', friendsNetListViewSet)

urlpatterns = [
    # DFW工具列表
    path('', include(router.urls))
]
