from django.contrib import admin

from .models import DesignWorks


# Register your models here.
@admin.register(DesignWorks)
class DesignAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'title')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)

    # 筛选器
    list_filter = ('cate', 'author')  # 过滤器
    search_fields = ('title', 'cate', 'author')  # 搜索字段
    date_hierarchy = 'createtime'  # 详细时间分层筛选　

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            # '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )


# admin.site.register(Desgin)
admin.site.site_header = '5windy个人网站后台管理系统'  # admin头名称
admin.site.site_title = 'Windy后台管理系统'
