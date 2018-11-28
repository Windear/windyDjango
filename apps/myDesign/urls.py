from django.urls import path, include
from myDesign.views import DesignListViewSet,DesignDetailViewSet
from rest_framework.routers import DefaultRouter

app_name = 'myDesign'

router = DefaultRouter()

# 配置resource的URL
router.register(r'designList', DesignListViewSet)
router.register(r'designDetail', DesignDetailViewSet)

urlpatterns = [
    # DFW
    path('', include(router.urls))
]
