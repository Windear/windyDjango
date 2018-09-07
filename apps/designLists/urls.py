from django.urls import path, re_path
from designLists.uploads import upload_image
from . import views


app_name = 'designLists'
urlpatterns = [
    # 所有项目
    path('', views.designLists),
    # 设计分类
    path('cate', views.get_design_cate),
    # 设计列表
    path('designList', views.get_design_list),
    # 项目列表
    path('project', views.post_project_list),
    # 设计详情
    path('details/<int:id>', views.get_design_detail),
    # 案例列表
    path('caseList', views.get_case_list),

]
