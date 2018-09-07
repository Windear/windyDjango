from django.db import models
# 定义上传文件的名称工具
from werkzeug.utils import secure_filename
import os, datetime, uuid


class Desgin(models.Model):
    """
    设计详情表
    1.编号id
    2.标题
    3.分类
    4.设计时间
    5.作者
    6.版权
    7. 封面
    8.简介
    9.内容
    10.发布人
    11.发布时间
    12.修改人
    13.修改时间
    14.删除人
    15.删除时间
    """
    CATEGORY_TYPE = (
        (1, "UI设计"), (2, "插画/原画"), (3, "平面设计"), (4, "3D设计"), (5, "动效设计")
    )

    # 自定义 上传图片的保存路径和，图片名称格式。
    # 修改文件名称
    def change_name(name):
        # 获取文件名称
        info = os.path.splitext(name)

        # 文件名格式：时间格式字符串+唯一字符串+后缀名
        file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + info[-1]
        #print(file_name)
        return file_name

    def upload_path_handler(instance, file_name):
        # 图片名称
        #file = secure_filename(file_name)
        filename = Desgin.change_name(file_name)
        return "designImg/{file}".format(file=filename)  # 保存路径和格式

    title = models.CharField(max_length=100, verbose_name="作品标题")
    cate = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="设计类别", help_text="设计类别")
    dgndatetime = models.CharField(blank=True, max_length=100, null=True, verbose_name="设计时间")
    author = models.CharField(max_length=100, verbose_name="作者")
    copyright = models.CharField(max_length=100, verbose_name="版权")
    picture = models.ImageField('展示图', upload_to=upload_path_handler, max_length=100)
    introduction = models.CharField(max_length=300, blank=True, null=True, verbose_name="设计简介")
    content = models.TextField()
    createman = models.CharField(max_length=100, verbose_name="创建人")
    createtime = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    updateman = models.CharField(max_length=100, blank=True, null=True, verbose_name="修改人")
    updatetime = models.DateTimeField(blank=True, null=True, verbose_name="修改时间")
    deleteman = models.CharField(max_length=100, blank=True, null=True, verbose_name="删除人")
    deletetime = models.DateTimeField(blank=True, null=True, verbose_name="删除时间")

    class Meta:
        managed = False
        db_table = 'desgin'
        verbose_name = "设计列表"  # 单数数据表可读名称
        verbose_name_plural = "设计列表"  # 复数数据表可读名称

    def __str__(self):
        return self.title
