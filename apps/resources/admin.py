from django.contrib import admin

from resources.models import Resources, CloudDrive


# Register your models here.
class CloudDriveInline(admin.StackedInline):
    model = CloudDrive
    extra = 1  #默认关联3个，这里调整至1个

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):

    #外键关联
    inlines = [
        CloudDriveInline,
    ]
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'title', 'cate', 'download_num', 'looked_num')
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
