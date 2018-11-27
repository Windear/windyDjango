# Generated by Django 2.0.4 on 2018-11-26 03:11

import DjangoUeditor.models
import designLists.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desgin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='作品标题')),
                ('cate', models.IntegerField(choices=[(1, 'UI设计'), (2, '插画/原画'), (3, '平面设计'), (4, '3D设计'), (5, '动效设计')], help_text='设计类别', verbose_name='设计类别')),
                ('dgndatetime', models.CharField(blank=True, max_length=100, null=True, verbose_name='设计时间')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('copyright', models.CharField(max_length=100, verbose_name='版权')),
                ('picture', models.ImageField(upload_to=designLists.models.Desgin.upload_path_handler, verbose_name='展示图')),
                ('introduction', models.CharField(blank=True, max_length=300, null=True, verbose_name='设计简介')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容\t')),
                ('active', models.IntegerField(blank=True, choices=[(0, '显示'), (1, '隐藏')], default=0, help_text='是否显示', verbose_name='是否显示')),
                ('createman', models.CharField(max_length=100, verbose_name='创建人')),
                ('createtime', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('updateman', models.CharField(blank=True, max_length=100, null=True, verbose_name='修改人')),
                ('updatetime', models.DateTimeField(blank=True, null=True, verbose_name='修改时间')),
                ('deleteman', models.CharField(blank=True, max_length=100, null=True, verbose_name='删除人')),
                ('deletetime', models.DateTimeField(blank=True, null=True, verbose_name='删除时间')),
            ],
            options={
                'verbose_name': '设计列表',
                'verbose_name_plural': '设计列表',
                'db_table': 'desgin'
            },
        ),
    ]
