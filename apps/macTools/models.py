from django.db import models
import os, datetime, uuid


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


# # 上传素材文件
# def upload_resource(instance, file_name):
#     filename = change_name(file_name)
#     return "resourceFile/{file}".format(file=filename)  # 保存路径和格式


class Tools(models.Model):
    """
    1.icon 工具icon
    2.title 标题
    3.cate 类别
    4.tag 关键词
    5.introduction 介绍
    6.looked_num 浏览量
    7.download_num 下载量
    8.new_version 最新版本
    9.content 详情
    10.active 是否激活
    11.create_id
    12.create_time
    13.edit_id
    14.edit_time
    15.delete_id
    16.delete_time
    """

    CATEGORY_TYPE = (
        (1, "应用软件"), (2, "媒体工具"), (3, "网络工具"), (4, "开发工具"), (5, "设计工具"), (6, "行业软件"), (7, "安全防护"), (8, "系统工具"),
        (9, "免费精品"),
        (10, "其他")
    )

    icon = models.ImageField('展示图', upload_to=upload_path_handler, max_length=100)
    title = models.CharField(max_length=100, verbose_name="工具标题")
    new_version = models.CharField(max_length=100, verbose_name="最新版本")
    cate = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="工具类别", help_text="工具类别")
    tag = models.CharField(max_length=300, verbose_name="标签")
    introduction = models.CharField(max_length=300, blank=True, null=True, verbose_name="工具简介")
    content = models.TextField()
    download_num = models.IntegerField(default=0, verbose_name="下载次数", help_text="下载次数")
    looked_num = models.IntegerField(default=0, verbose_name="浏览量", help_text="浏览量")

    active = models.BooleanField(default=True, verbose_name="是否显示", help_text="是否显示")
    create_id = models.CharField(max_length=100, verbose_name="创建人")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    edit_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="修改人")
    edit_time = models.DateTimeField(blank=True, null=True, verbose_name="修改时间")
    delete_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="删除人")
    delete_time = models.DateTimeField(blank=True, null=True, verbose_name="删除时间")

    class Meta:
        verbose_name = "工具详情"  # 单数数据表可读名称
        verbose_name_plural = "工具列表"  # 复数数据表可读名称

    def __str__(self):
        return self.title


class HistoryVersion(models.Model):
    """
    0.所属工具  macTools
    1.version 版本号
    2.language 语言
    3.update_time 更新时间
    4.file_size 文件大小
    5.drive_type 网盘类型
    6.drive_url 网盘链接
    7.drive_pw 网盘密码
    """
    CLOUD_TYPE = ((1, "百度网盘"), (2, "360网盘"), (3, "115网盘"))
    LANGUAGE_TYPE = (("CH", "中文"), ("EN", "英文"))

    tools = models.ForeignKey(Tools, on_delete=models.CASCADE, verbose_name="所属工具")
    version = models.CharField(max_length=100, verbose_name="版本")
    language = models.CharField(choices=LANGUAGE_TYPE, max_length=100, verbose_name="语言", help_text="工具语言")
    update_time = models.DateTimeField(blank=True, null=True, verbose_name="更新时间")
    file_size = models.CharField(max_length=100, verbose_name="文件大小")
    drive_type = models.IntegerField(choices=CLOUD_TYPE, default=1, verbose_name="网盘类型", help_text="网盘类型")
    drive_url = models.CharField(max_length=100, blank=True, null=True, verbose_name="网盘下载链接")
    drive_pw = models.CharField(max_length=100, blank=True, null=True, verbose_name="网盘密码")

    class Meta:
        verbose_name = "网盘链接"  # 单数数据表可读名称
        verbose_name_plural = "网盘链接"  # 复数数据表可读名称

    def __int__(self):
        return self.id