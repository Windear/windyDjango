from django.db import models
# 定义上传文件的名称工具
from werkzeug.utils import secure_filename
import os, datetime, uuid


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
    # print(file_name)
    # file = secure_filename(file_name)
    filename = change_name(file_name)
    return "resourceImg/{file}".format(file=filename)  # 保存路径和格式


# 上传素材文件
def upload_resource(instance, file_name):
    # print(file_name)
    # file = secure_filename(file_name)
    filename = change_name(file_name)
    return "resourceFile/{file}".format(file=filename)  # 保存路径和格式


class Resources(models.Model):
    """
    1.标题  title
    2.分类  cate
    3.作者  author
    4.版权  copyright
    5.展示图  picture
    6.介绍  introduction
    7.详情  content
    8.标签  tag
    9.下载次数  download_num
    10.浏览量  looked_num
    11.文件类型  file_type
    12.下载链接 download_address

    13.是否激活 active
    14.创建人  create_id
    15.创建时间  create_time
    16.修改人  edit_id
    17.修改时间  edit_time
    18.删除人  delete_id
    19.删除时间  delete_time
    """

    CATEGORY_TYPE = (
        (1, "UI"), (2, "线性icon"), (3, "彩色icon"), (4, "UI Kit"), (5, "写实"), (6, "插画"), (7, "电商"), (8, "交互"), (9, "报表"),
        (10, "GIF"), (11, "C4D"),(12,"Mockup"),(13,"平面设计")
    )

    title = models.CharField(max_length=100, verbose_name="素材标题")
    cate = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="素材类别", help_text="素材类别")
    author = models.CharField(max_length=100, verbose_name="作者")
    copyright = models.CharField(max_length=100, verbose_name="版权")
    picture = models.ImageField('展示图', upload_to=upload_path_handler, max_length=100)
    introduction = models.CharField(max_length=300, blank=True, null=True, verbose_name="素材简介")
    content = models.TextField()
    tag = models.CharField(max_length=100, verbose_name="标签")
    download_num = models.IntegerField(default=0, verbose_name="下载次数", help_text="下载次数")
    looked_num = models.IntegerField(default=0, verbose_name="浏览量", help_text="浏览量")
    file_type = models.CharField(max_length=100, verbose_name="文件类型", default="sketch")
    download_address = models.FileField(upload_to=upload_resource, max_length=100, verbose_name="下载链接")

    active = models.BooleanField(default=True, verbose_name="是否显示", help_text="是否显示")
    createman = models.CharField(max_length=100, verbose_name="创建人")
    createtime = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    updateman = models.CharField(max_length=100, blank=True, null=True, verbose_name="修改人")
    updatetime = models.DateTimeField(blank=True, null=True, verbose_name="修改时间")
    deleteman = models.CharField(max_length=100, blank=True, null=True, verbose_name="删除人")
    deletetime = models.DateTimeField(blank=True, null=True, verbose_name="删除时间")

    class Meta:
        verbose_name = "素材详情"  # 单数数据表可读名称
        verbose_name_plural = "素材列表"  # 复数数据表可读名称

    def __str__(self):
        return self.title


class CloudDrive(models.Model):
    """
    网盘链接
    1.所属素材 resources
    2.网盘类型 drive_type
    3.网盘下载链接 drive_url
    4.网盘密码 drive_pw
    """
    CLOUD_TYPE = ((1, "百度网盘"), (2, "360网盘"), (3, "115网盘"))
    resources = models.ForeignKey(Resources, on_delete=models.CASCADE, verbose_name="所属素材")
    drive_type = models.IntegerField(choices=CLOUD_TYPE, default=1, verbose_name="网盘类型", help_text="网盘类型")
    drive_url = models.CharField(max_length=100, blank=True, null=True, verbose_name="网盘下载链接")
    drive_pw = models.CharField(max_length=100, blank=True, null=True, verbose_name="网盘密码")

    class Meta:
        verbose_name = "网盘链接"  # 单数数据表可读名称
        verbose_name_plural = "网盘链接"  # 复数数据表可读名称

    def __int__(self):
        return self.id
