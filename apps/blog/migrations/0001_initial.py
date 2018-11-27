# Generated by Django 2.0.4 on 2018-11-26 03:08

import DjangoUeditor.models
import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(max_length=200, upload_to=blog.models.upload_path_handler, verbose_name='文章首图')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('introduction', models.CharField(blank=True, max_length=300, null=True, verbose_name='文章简介')),
                ('cate', models.IntegerField(choices=[(1, '设计分享'), (2, '前端分享'), (3, '后端分享'), (4, '经验分享'), (5, '工具配置')], help_text='文章类别', verbose_name='文章类别')),
                ('tag', models.CharField(max_length=300, verbose_name='标签')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('is_original', models.IntegerField(choices=[(1, '原创'), (2, '转载')], default=1, help_text='是否原创', verbose_name='是否原创')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容\t')),
                ('looked_num', models.IntegerField(default=0, help_text='浏览量', verbose_name='浏览量')),
                ('active', models.BooleanField(default=True, help_text='是否显示', verbose_name='是否显示')),
                ('create_id', models.CharField(max_length=100, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('edit_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='修改人')),
                ('edit_time', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
                ('delete_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='删除人')),
                ('delete_time', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
            ],
            options={
                'verbose_name': '文章详情',
                'verbose_name_plural': '文章列表',
            },
        ),
    ]
