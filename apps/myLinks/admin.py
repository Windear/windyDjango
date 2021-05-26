from django.contrib import admin

from myLinks.models import Friends_net, Collection_net


# Register your models here.

@admin.register(Collection_net)
class CollectionNetAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'net_name', 'link_url')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 8
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)

    # 筛选器
    # list_filter = ('cate', 'is_original')  # 过滤器
    # search_fields = ('title', 'cate')  # 搜索字段
    # date_hierarchy = 'create_time'  # 详细时间分层筛选　

@admin.register(Friends_net)
class FriendsNetAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'net_name', 'link_url')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 8
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)
