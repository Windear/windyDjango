"""windyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve
from designLists.uploads import upload_image
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),

    # dfw配置
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # dfw文档
    path('docs/', include_docs_urls(title='有爱设计API文档')),

    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls', namespace='users')),
    path('design/', include('apps.designLists.urls', namespace='designLists')),
    path('resources/', include('apps.resources.urls', namespace='resources')),
    path('tools/', include('apps.macTools.urls', namespace='tools')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('myLinks/', include('apps.myLinks.urls', namespace='myLinks')),
    # 上传图片
    re_path('^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    re_path("^media/(?P<path>.*)$", serve,
            {"document_root": settings.MEDIA_ROOT, }),
    re_path(r'^ueditor/', include('DjangoUeditor.urls')),

]
urlpatterns += staticfiles_urlpatterns()