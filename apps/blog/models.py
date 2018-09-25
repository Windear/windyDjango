from django.db import models
import os, datetime, uuid
from DjangoUeditor.models import UEditorField


# Create your models here.

# Create your models here.
# 自定义 上传图片的保存路径和，图片名称格式。
# 修改文件名称
def change_name(name):
    # 获取文件名称
    info = os.path.splitext(name)
    # 文件名格式：时间格式字符串+唯一字符串+后缀名
    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + info[-1]
    print(info)
    return file_name


# 上传展示图
def upload_path_handler(instance, file_name):
    # 图片名称
    filename = change_name(file_name)
    return "toolsImg/{file}".format(file=filename)  # 保存路径和格式


# 文章
class BlogArticle(models.Model):
    """
       1.picture 首图
       2.title 标题
       3.introduction 介绍
       4.cate 类别
       5.tag 关键词
       6.author 作者
       7.is_original 是否原创
       8.content 正文
       9.looked_num 浏览量

       10.active 是否激活
       11.create_id
       12.create_time
       13.edit_id
       14.edit_time
       15.delete_id
       16.delete_time
       """

    CATEGORY_TYPE = (
        (1, "设计分享"), (2, "前端分享"), (3, "后端分享"), (4, "经验分享"), (5, "工具配置")
    )
    IS_ORIGINAL = ((1, "原创"), (2, "转载"))

    picture = models.ImageField('文章首图', upload_to=upload_path_handler, max_length=200)
    title = models.CharField(max_length=100, verbose_name="文章标题")
    introduction = models.CharField(max_length=300, blank=True, null=True, verbose_name="文章简介")
    cate = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="文章类别", help_text="文章类别")
    tag = models.CharField(max_length=300, verbose_name="标签")
    author = models.CharField(max_length=100, verbose_name="作者")
    is_original = models.IntegerField(choices=IS_ORIGINAL, default=1, verbose_name="是否原创", help_text="是否原创")

    content = UEditorField(u'内容	', width=900, height=600, toolbars="full", imagePath="blogImg/",
                           filePath="blogFile/",
                           upload_settings={"imageMaxSize": 1204000, "catcherPathFormat": "blogImg/"},
                           settings={}, command=None, blank=True, )

    looked_num = models.IntegerField(default=0, verbose_name="浏览量", help_text="浏览量")

    active = models.BooleanField(default=True, verbose_name="是否显示", help_text="是否显示")
    create_id = models.CharField(max_length=100, verbose_name="创建人")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    edit_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="修改人")
    edit_time = models.DateTimeField(blank=True, null=True, verbose_name="修改时间")
    delete_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="删除人")
    delete_time = models.DateTimeField(blank=True, null=True, verbose_name="删除时间")

    class Meta:
        verbose_name = "文章详情"  # 单数数据表可读名称
        verbose_name_plural = "文章列表"  # 复数数据表可读名称

    def __str__(self):
        return self.title


