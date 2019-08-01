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
    #print(info)
    return file_name


# 上传展示图
def upload_path_handler(instance, file_name):
    # 图片名称
    filename = change_name(file_name)
    return "linkImg/{file}".format(file=filename)  # 保存路径和格式


class Collection_net(models.Model):
    """
    1.icon
    2.net_name
    3.link_url
    """
    icon = models.ImageField('链接ico', upload_to=upload_path_handler, max_length=300)
    net_name = models.CharField(max_length=100, verbose_name="网站名称")
    link_url = models.CharField(max_length=500, blank=True, null=True, verbose_name="网站链接")

    class Meta:
        verbose_name = "收藏网站"  # 单数数据表可读名称
        verbose_name_plural = "收藏网站"  # 复数数据表可读名称

    def __str__(self):
        return self.net_name


class Friends_net(models.Model):
    """
    1.net_name
    2.link_url
    """
    net_name = models.CharField(max_length=100, verbose_name="网站名称")
    link_url = models.CharField(max_length=500, blank=True, null=True, verbose_name="网站链接")

    class Meta:
        verbose_name = "友情链接"  # 单数数据表可读名称
        verbose_name_plural = "友情链接"  # 复数数据表可读名称

    def __str__(self):
        return self.net_name
